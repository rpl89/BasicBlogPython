from django.contrib import admin
from blog.models import Categoria, Articulo, Comentario


admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Comentario)
