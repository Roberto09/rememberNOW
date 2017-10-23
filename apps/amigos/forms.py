# -*- encoding:utf-8 -*-
from django import forms

class BusquedaUser(forms.Form):
	busqueda_usuario=forms.CharField(label="Buscar por usuario", max_length=20)