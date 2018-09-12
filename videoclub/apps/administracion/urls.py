from django.conf.urls import patterns, url 
from apps.administracion.views import Administracion, PeliculaList, PeliculaDetail, PeliculaCreation, PeliculaUpdate, PeliculaDelete, UsuarioList, UsuarioDetail, UsuarioCreation, UsuarioUpdate, UsuarioDelete



urlpatterns= patterns('',
	url(r'^$', Administracion.as_view(),name='admin'),
   
    url(r'^pelicula/$', PeliculaList.as_view(), name='list'),
    url(r'^pelicula/(?P<pk>\d+)$', PeliculaDetail.as_view(), name='detail'),
    url(r'^pelicula/nuevo$', PeliculaCreation.as_view(), name='new'),
    url(r'^pelicula/editar/(?P<pk>\d+)$', PeliculaUpdate.as_view(), name='edit'),
    url(r'^pelicula/borrar/(?P<pk>\d+)$', PeliculaDelete.as_view(), name='delete'),  
    
    url(r'^usr/$', UsuarioList.as_view(), name='listUsr'),
    url(r'^usr/(?P<pk>\d+)$', UsuarioDetail.as_view(), name='detailUsr'),
    url(r'^usr/nuevo$', UsuarioCreation.as_view(), name='newUsr'),
    url(r'^usr/editar/(?P<pk>\d+)$', UsuarioUpdate.as_view(), name='editUsr'),
    url(r'^usr/borrar/(?P<pk>\d+)$', UsuarioDelete.as_view(), name='deleteUsr'),
)


    