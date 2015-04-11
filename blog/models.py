from django.db import models
from django.contrib.auth.models import User


class Usuario(User): ##CLASE 'Usuario': Continene el nombre de los usuarios existentes REALES

	def __unicode__(self):
		return self.username ## FUNCION QUE DEVUELVE EL USUARIO COMO IDENTIFICADOR DE LA CLASE

class Categoria(models.Model): ##CLASE 'Articulo': Contiene las caracteristicas de un articulo como son titulo, contenido, categoria y fecha
    name = models.CharField(max_length=200)
    
    def __unicode__(self): ## FUNCION QUE DEVUELVE LA CATEGORIA COMO IDENTIFICADOR DE LA CLASE
        return self.name

class Articulo(models.Model): ##CLASE 'Articulo': contiene las caracteristicas de un articulo como son: contenido, categoria, fecha y titulo
    titulo = models.CharField(max_length=200)
    contenido = models.TextField() ## Campo de texto
    categoria = models.ForeignKey(Categoria) ## Clave foranea con Categoria
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self): ## FUNCION QUE DEVUELVE EL ARTICULO COMO IDENTIFICADOR DE LA CLASE
        return self.titulo

class Comentario(models.Model): ##CLASE 'Comentario': contiene las caracteristicas de un articulo, nombre, texto, fecha 
 
    articulo = models.ForeignKey(Articulo)
    nombre = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self): ## FUNCION QUE DEVUELVE EL COMENTARIO COMO IDENTIFICADOR DE LA CLASE
        return self.texto

