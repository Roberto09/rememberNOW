from django.conf.urls import url, include
from apps.amigos.views import BuscarAmigos, AgregarAmigos, ListaAmigos
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #url(r'^buscar_amigos$', BuscarAmigos , name='buscar_amigos'),
    url(r'^buscar_amigos/(?P<userentry>\w+)/$', login_required(BuscarAmigos), name='buscar_amigos_search'),
    url(r'^buscar_amigos/$', login_required(BuscarAmigos), name='buscar_amigos'),
    url(r'^agregar_amigo/(?P<id_usuario>\d+)/$', login_required(AgregarAmigos), name='agregar_amigos'),
    url(r'^mis_amigos/$', login_required(ListaAmigos.as_view()), name='lista_amigos'),
]