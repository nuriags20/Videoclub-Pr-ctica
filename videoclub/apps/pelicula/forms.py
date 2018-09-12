from django import forms
from apps.pelicula.models import Pelicula

class PeliculaForm(forms.ModelForm):
	
	class Meta:
		model = Pelicula
		
		fields = [
			'titulo',
			'video',
			'descripcion',
			'año',
			'director',
			'reparto',
			'portada',
			'valoracion',
			'etiqueta',
		]


		labels={
			'titulo': 'Titulo',
			'video': 'Video',
			'descripcion': 'Descripcion',
			'año':'Año',
			'director':'Director',
			'reparto': 'Reparto',
			'portada':'Portada',
			'valoracion':'Valoracion',
			'etiqueta' : 'Etiqueta'
		}
		
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'video': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'año':forms.TextInput(attrs={'class':'form-control'}),
			'director':forms.TextInput(attrs={'class':'form-control'}),
			'portada': forms.TextInput(attrs={'class':'form-control'}),
			'reparto': forms.TextInput(attrs={'class':'form-control'}),
			'valoracion':forms.TextInput(attrs={'class':'form-control'}),
			'etiqueta':forms.TextInput(attrs={'class':'form-control'}),
		}