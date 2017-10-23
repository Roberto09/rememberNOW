from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
	#link a propiedades de usuario
	propiedades_usuario=models.OneToOneField(User, on_delete=models.CASCADE,related_name='propiedades_usuario+')
	#otras propiedades
	pregunta_app=models.CharField(max_length=30, blank=True, null=True,)
	amigos=models.ManyToManyField(User, blank=True, related_name='amigos_+' )