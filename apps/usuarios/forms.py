# -*- encoding:utf-8 -*-
from django import forms

from apps.usuarios.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm (forms.ModelForm):
	class Meta:
		model = Usuario
		
		fields = [
		'pregunta_app',
		]

		labels= {
		'pregunta_app':'How did you find out about rememberNOW?(optional)',
		}
		widgets={
		'pregunta_app': forms.TextInput(attrs={'class':'form-control'}),
		}

class UserDataForm (UserCreationForm):
	class Meta:
		model = User

		fields = [
		'first_name',
		'last_name',
		'username',
		'email',
		]

		labels= {
		'first_name':'Name: ',
		'last_name': 'Last name: ',
		'username':'Username: ',
		'email':'E-mail: ',
		}

		widgets={
		'first_name': forms.TextInput(attrs={'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'class':'form-control'}),
		'username': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.TextInput(attrs={'class':'form-control'}),
		}