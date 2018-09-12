from django.conf.urls import patterns, url 
from apps.pelicula.views import pelicula_id, pelicula_filtro, pelicula_list


urlpatterns= patterns('',
	url(r'^listadoPeliculas/$', pelicula_list, name='pelicula_list'),
  	url(r'^(?P<etiqueta>[-\w]+)/$', pelicula_filtro, name='pelicula_filtro'),
    url(r'^pelicula/(?P<pk>[0-9]+)/$', pelicula_id, name='pelicula_id'),
    
)


    