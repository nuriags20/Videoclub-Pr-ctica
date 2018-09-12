from django.conf.urls import patterns, url
from .views import Logout, peliculas, search

urlpatterns= patterns('',
	url(r'^$', peliculas, name='videoclub'),
	url(r'^search', search, name='search'),
	url(r'^salir', Logout.as_view(), name='logout'),
	
)