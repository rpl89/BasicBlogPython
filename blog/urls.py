from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    # Define el acceso a las vistas de articulos y los detalles de cada una, borrar, nuevos comentarios, categorias, etc.
	url(r'^$', 'blog.views.home', name='home'),
    url(r'^articulo/(?P<idarticulo>[0-9]+)/$', 'blog.views.articulo', name="articulo"),
    url(r'^articulo/nuevo$','blog.views.nuevoArticulo'),
    url(r'^articulo/(?P<idarticulo>[0-9]+)/borrar$', 'blog.views.borrar', name="borrar"),
    url(r'^articulo/(?P<idarticulo>[0-9]+)/comentario$','blog.views.nuevoComentario'),
    url(r'^categoria/(?P<idcategoria>[0-9]+)/$', 'blog.views.categoria', name="categoria"),
    url(r'^registro$','blog.views.registro'),
#    url(r'^comentario$','blog.views.nuevoComentario'),

    # Define el acceso a las vistas de autentificacion y des-autentificacion
    url(r'^login$','blog.views.logueo'),
	url(r'^logout$','blog.views.deslogueo'),
	url(r'^error/$','blog.views.error'),

	#url(r'^borrar/(?P<idarticulo>\\d+)/$', 'borrar'),
)
