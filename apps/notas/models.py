from django.db import models
from django.contrib.auth.models import User
from apps.grupos.models import Grupo

# Create your models here.
class Nota_individual(models.Model):
	titulo=models.CharField(max_length=20)
	contenido=models.TextField(max_length=150)
	usuario_nota=models.ForeignKey(User)


class Nota_grupal(models.Model):
	titulo=models.CharField(max_length=20)
	contenido=models.TextField(max_length=150)
	grupo=models.ForeignKey(Grupo)
	creador_nota=models.ForeignKey(User)