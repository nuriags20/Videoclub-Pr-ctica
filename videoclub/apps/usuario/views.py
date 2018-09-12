from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from .forms import RegistroForm

# Create your views here.

class Registro(CreateView):
	model = User
	template_name= "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('usuario:registroOk')
	
class RegistroOk(TemplateView):
    template_name = "usuario/registroOk.html"