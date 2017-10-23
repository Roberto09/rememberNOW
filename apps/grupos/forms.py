from django import forms
from apps.grupos.models import Grupo

class GrupoForm(forms.ModelForm):
	class Meta:
		model = Grupo

		fields = [
		'Nombre',
		'Descripcion',
		'integrantes',
		]

		labels = {
		'Nombre': 'Name of the Group',
		'Descripcion': 'Describe the Group (optional)',
		'integrantes': 'Add friends to your group',
		}

		widgets = {
		'Nombre': forms.TextInput(attrs={'class':'form-control'}),
		'Descripcion': forms.TextInput(attrs={'class':'form-control'}),
		'integrantes': forms.CheckboxSelectMultiple(),
		}