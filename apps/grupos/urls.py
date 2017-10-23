from django.conf.urls import url, include
from apps.grupos.views import CrearGrupo, VerGrupos
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear_grupos$', login_required(CrearGrupo.as_view()) , name='crear_grupos'),
    url(r'^ver_grupos$', login_required(VerGrupos.as_view()) , name='ver_grupos'),
]