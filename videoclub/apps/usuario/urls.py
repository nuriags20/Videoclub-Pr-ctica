from django.conf.urls import patterns, url
from apps.usuario.views import Registro, RegistroOk

urlpatterns= patterns('',
	url(r'^registrar/', Registro.as_view(), name='registrar'),
	url(r'^usrValido/', RegistroOk.as_view(), name='registroOk'),
	
	
)