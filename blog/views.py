

from django.http import HttpResponse, HttpResponseRedirect ## Importa HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout ##Importa librerias de login, autenticate, logout
from django.contrib.auth.models import User ##Importa el modelo user
from django.contrib.auth.forms import AuthenticationForm ##Importa modelo del formulario autentication
from django.shortcuts import render_to_response, get_object_or_404, render, redirect ## Importa la clase render, redirect y error_404 con el que se devuelve el contenido al template
from django.template import RequestContext 
from blog.models import Categoria, Articulo, Comentario ## Importa las clases creadas en nuestro modelo
from blog.forms import formNuevoUsuario, formNuevoArticulo, formNuevoComentario ## Importa el formulario de NuevoUsuario, NuevoArticulo, NuevoComentario


def home(request):
    articulos = Articulo.objects.order_by("-fecha") 
    datosPlantilla = {'articulos':articulos}
    return render(request,'home.html',datosPlantilla) ##Se devuelve la informacion al template

def error(request):
    return render(request,'error.html',None) 

def articulo(request, idarticulo):
    articulo = Articulo.objects.get(id = idarticulo)
    comentarios = Comentario.objects.filter(articulo = articulo)
    datosPlantilla = {'articulo':articulo,'comentarios':comentarios}
    return render(request,'articulo.html',datosPlantilla) ## Se devuelve la informacion al template


def borrar(request, idarticulo):
    articulo = Articulo.objects.get(id = idarticulo)
    articulo.delete()
    return HttpResponseRedirect('/') ##Se redirige al index


def categoria(request, idcategoria):
    categoria = Categoria.objects.get(id = idcategoria)
    articulos = categoria.articulo_set.order_by("-fecha")
    datosPlantilla = {'articulos':articulos}
    return render(request,'home.html',datosPlantilla) ## Se devuelve la informacion al template


def nuevoArticulo(request):
    if request.user.is_anonymous(): 
        return HttpResponseRedirect('/') 
    else:
        if request.method== 'POST': ## En caso de que recibamos informacion del formulario
            formulario=formNuevoArticulo(request.POST,request.FILES) 
            elForm = formulario.save(commit = False)
            if formulario.is_valid(): ##En caso de que el formulario sea correcto, guardamos los datos y redirigimos al usuario
                formulario.save() ## Guarda el formulario
                return HttpResponseRedirect('/') # Se redirige al index
        else: 
            formulario=formNuevoArticulo()
        datosPlantilla={'formulario':formulario}
        return render(request,'nuevoArticulo.html', datosPlantilla) ## Se devuelve la informacion al template


def nuevoComentario(request, idarticulo):
    if request.method=='POST': ## En caso de que recibamos informacion del formulario
        formulario = formNuevoComentario(request.POST) 
        if formulario.is_valid(): ## En caso de que el formulario sea correcto, guardamos los datos y redirigimos al usuario
            comentario = formulario.save(commit = False) 
            comentario.articulo = Articulo.objects.get(id = idarticulo)
            comentario.save() ## Guarda el formulario
            return HttpResponseRedirect('/articulo/'+idarticulo) 
    else:
        formulario = formNuevoComentario()
    
    datosPlantilla = {'formulario':formulario}
    return render(request,'nuevoComentario.html',datosPlantilla) ## Se devuelve la informacion al template


def registro(request):
    if request.method=='POST': ##En caso de que recibamos informacion del formulario
        formulario = formNuevoUsuario(request.POST)  
        if formulario.is_valid: ##En caso de que el formulario sea correcto, guardamos los datos y redirigimos al usuario
            formulario.save() ##Guarda el formulario
            return HttpResponseRedirect('/') ## Se redirige al index
    else:
        formulario = formNuevoUsuario() ##Prepara el formulario nuevo usuario en la clase formulario

    datosPlantilla = {'formulario':formulario}
    return render(request,'registro.html',datosPlantilla) ## Se devuelve la informacion al template


def logueo(request):
    if request.method=='POST': ## En caso de que recibamos informacion del formulario
        formulario = AuthenticationForm(request.POST) 
        if formulario.is_valid:  ##En caso de que el formulario sea correcto, verificamos los datos del usuario
            acceso = authenticate(username=request.POST['username'], password=request.POST['password']) ##Obtenemos el nombre de usuario ## Obtenemos la clave de usuario ## Autenticamos al usuario contra el sistema
            if acceso is not None: ###Si tiene acceso, es decir, existe en la tabla
                if acceso.is_active:  ##Si esta activo
                    login(request, acceso) ##Se identifica
                    return HttpResponseRedirect('/') ## Se redirige al index
                else:
                    return HttpResponseRedirect('/error') ## EL usuario esta no esta activado se produce error
            else:
                return HttpResponseRedirect('/error') ## EL usuario esta no esta activado se produce error
    else:
        formulario = AuthenticationForm() ## Prepara el formulario en la clase AutenticationForm

    datosPlantilla = {'formulario':formulario} 
    return render(request,'login.html',datosPlantilla) ## Se devuelve la informacion al template


def deslogueo(request):
    logout(request)  ##Se desloguea el usuario
    return HttpResponseRedirect('/') ## Se redirige al index