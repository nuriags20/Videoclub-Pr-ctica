from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth.views import logout
from apps.pelicula.forms import Pelicula
from apps.pelicula.views import pelicula_id, pelicula_filtro, mediaValoracion

# Create your views here.
class Logout(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)
 
def peliculas(request):
	etiqueta=['Estrenos','Comedia','Drama', 'Infantil']
	peliculas=[]
	lista=[]
	#Lista de sublistas de ultimas 4 películas para cada etiqueta
	for etiq in etiqueta:
		lista.append(Pelicula.objects.filter(etiqueta=etiq)[:4])
	
	#Creamos una lista, que contenga 16 películas para que se muestren en videoclub.html
	for x in lista:
		for i in x:
			peliculas.append(i)
			
	contexto = {'etiquetas': etiqueta, 'peliculas': peliculas}
	return render(request, 'pagVideoclub/videoclub.html', contexto)
	
def search(request):
	titulo = request.GET.get('titulo')
	try:	
		pelicula = Pelicula.objects.get(titulo=titulo)
		if request.method == 'POST':
			voto = request.POST['valoracion']
			valoracionFinal = mediaValoracion(pelicula.valoracion, int(voto))
			pelicula.valoracion = valoracionFinal
			pelicula.save()
			return render(request, 'pelicula/pelicula_id.html', {'pelicula': pelicula})
		else:
			return render(request,'pelicula/pelicula_id.html', {'pelicula': pelicula})
	except: 
		return render(request,'pagVideoclub/errorBusqueda.html')
