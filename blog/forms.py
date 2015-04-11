#encoding: utf-8

from blog.models import Usuario, Articulo, Comentario # Importa las clases de nuestro modelo
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm # Importa el modelo de formularios
from django import forms


class formNuevoUsuario(UserCreationForm):
	class Meta:
		model = Usuario # Crea el formulario con nuestro modelo
		fields = ('username',)

class formNuevoArticulo(ModelForm):
	class Meta:
		model = Articulo # Crea el formulario con nuestro modelo
		fields = ('titulo','contenido','categoria')

	def __init__(self, *args, **kwargs):
		super(ModelForm,self).__init__(*args,**kwargs)
		self.fields['titulo'].widget.label='Titulo'  # Se le añade un sobrenombre a los campos de nuestro modelo

class formNuevoComentario(ModelForm):
	class Meta:
		model = Comentario # Crea el formulario con nuestro modelo
		fields = ('nombre', 'texto')
