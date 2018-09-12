from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.pelicula.forms import Pelicula
from django.contrib.auth.models import User
from apps.usuario.forms import RegistroForm

# Create your views here.

class Administracion(TemplateView):
    template_name = "auth/admin.html"
    
class PeliculaList(ListView):
    model = Pelicula

class PeliculaDetail(DetailView):
    model = Pelicula

class PeliculaCreation(CreateView):
    model = Pelicula
    success_url = reverse_lazy('administracion:list')
    fields = ['titulo','video','descripcion','año','director','reparto','portada','valoracion','etiqueta']

class PeliculaDelete(DeleteView):
    model = Pelicula
    success_url = reverse_lazy('administracion:list')

class PeliculaUpdate(UpdateView):
    model = Pelicula
    success_url = reverse_lazy('administracion:list')
    fields = ['titulo','video','descripcion','año','director','reparto','portada','valoracion','etiqueta']
    
class UsuarioList(ListView):
	model = User
	
class UsuarioDetail(DetailView):
    model = User

class UsuarioCreation(CreateView):
	model = User
	form_class = RegistroForm
	success_url = reverse_lazy('administracion:listUsr')

class UsuarioDelete(DeleteView):
    model = User
    success_url = reverse_lazy('administracion:listUsr')	

class UsuarioUpdate(UpdateView):
	model = User
	form_class = RegistroForm
	success_url = reverse_lazy('administracion:listUsr')