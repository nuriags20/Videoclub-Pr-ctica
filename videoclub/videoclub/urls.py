from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from .views import login_view

urlpatterns = [
  	url(r'^$', login_view, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^administracion/', include('apps.administracion.urls', namespace='administracion')),
    url(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
    url(r'^pelicula/', include('apps.pelicula.urls', namespace='pelicula')),
    url(r'^videoclub/', include('apps.pagVideoclub.urls', namespace='pagVideoclub')),  
    url(r'^reset/reseteoContraseña', password_reset, {'template_name':'resetearContraseña/reseteoPwdForm.html','email_template_name':'resetearContraseña/reseteoPwdEmail.html'}, name='password_reset'),
   	url(r'^reset/reseteoAvisoContraseña', password_reset_done, {'template_name':'resetearContraseña/reseteoPwdAviso.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'resetearContraseña/reseteoPwdConfir.html'}, name='password_reset_confirm'),
	url(r'^reset/reseteo', password_reset_complete, {'template_name':'resetearContraseña/reseteoPwd.html'}, name='password_reset_complete'),

]
