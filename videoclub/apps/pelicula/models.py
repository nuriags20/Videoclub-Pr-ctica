from django.db import models
from django.contrib import admin
# Create your models here.

class Pelicula(models.Model):
	titulo = models.CharField(max_length=150)
	video = models.URLField(max_length=350, blank=False)
	descripcion = models.TextField()
	año = models.IntegerField()
	director = models.CharField(max_length=150)
	reparto = models.CharField(max_length=200)
	portada = models.URLField(max_length=350, blank=False)
	valoracion = models.FloatField()
	etiqueta = models.CharField(max_length=50)
	

