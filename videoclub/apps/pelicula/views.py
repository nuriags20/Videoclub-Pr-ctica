from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from apps.pelicula.forms import Pelicula, PeliculaForm
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

   
def pelicula_list(request):
	peliculas = Pelicula.objects.all().order_by('titulo')
	return render(request, 'pelicula/listadoPeliculas.html',{'peliculas': peliculas})
	
def pelicula_filtro(request,etiqueta):
	pelicula = Pelicula.objects.filter(etiqueta=etiqueta).order_by('titulo')
	contexto = {'peliculas': pelicula, 'etiqueta':etiqueta}
	return render(request, 'pelicula/pelicula_filtro.html', contexto)

def pelicula_id(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
    	print(pelicula.valoracion)
    	voto = request.POST['valoracion']
    	print("voto: " + voto)
    	valoracionFinal = mediaValoracion(pelicula.valoracion, int(voto))
    	print(valoracionFinal)
    	pelicula.valoracion = valoracionFinal
    	print(pelicula.valoracion)
    	pelicula.save()
    	return render(request, 'pelicula/pelicula_id.html', {'pelicula': pelicula})
    else:
    	return render(request, 'pelicula/pelicula_id.html', {'pelicula': pelicula})

def mediaValoracion(valoracion, valoracionNew):
	valoracionFinal = (valoracion + valoracionNew)/2
	return "{0:.1f}".format(float(valoracionFinal))