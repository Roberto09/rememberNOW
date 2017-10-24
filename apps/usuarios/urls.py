from django.conf.urls import url, include
from apps.usuarios.views import prueba, Crear_Usuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^prueba', login_required(prueba), name='prueba'),
    url(r'^registrar', Crear_Usuario.as_view(), name="user_create"),


]