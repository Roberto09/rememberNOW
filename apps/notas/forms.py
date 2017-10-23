# -*- encoding:utf-8 -*-
from django import forms
from apps.notas.models import Nota_individual, Nota_grupal

class NotaIndividualForm(forms.ModelForm):
	class Meta:
		model=Nota_individual

		fields=[
		'titulo',
		'contenido',
		]

		labels={
		'titulo': 'Titulo de tu Nota.',
		'contenido': 'Escribe tu nota aqui.',
		}

		widgets={
		'titulo': forms.TextInput(attrs={'class':'form-control'}),
		'contenido': forms.Textarea(attrs={'class':'form-control'}),
		}

class NotaGrupalForm(forms.ModelForm):
	class Meta:
		model=Nota_grupal

		fields=[
		'titulo',
		'contenido',
		]

		labels={
		'titulo': 'Titulo de tu Nota.',
		'contenido': 'Escribe tu nota aqui.',
		}

		widgets={
		'titulo': forms.TextInput(attrs={'class':'form-control'}),
		'contenido': forms.Textarea(attrs={'class':'form-control'}),
		}
