from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario

# Create your models here.
class Grupo(models.Model):
	Creador_Grupo=models.ForeignKey(User, related_name='Creador_+')
	Nombre=models.CharField(max_length=30)
	Descripcion=models.TextField(max_length=100, blank=True, null=True,)
	integrantes=models.ManyToManyField(User)