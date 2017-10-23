from django.conf.urls import url, include
from apps.notas.views import CrearNotaInd, VerNotasInd, NotaIndDelete, NotaIndEdit, CrearNotaGrup, VerNotasGrup, NotaGrupDelete, NotaGrupEdit
from django.contrib.auth.decorators import login_required

urlpatterns = [
	#Notas Individuales
    url(r'^crear_nota_ind', login_required(CrearNotaInd.as_view()), name='crear_nota_ind'),
    url(r'^notas_ind', login_required(VerNotasInd.as_view()), name='notas_ind'),
    url(r'^borrar_nota_ind/(?P<pk>\d+)/$', login_required(NotaIndDelete.as_view()), name='borrar_nota_ind'),
    url(r'^editar_nota_ind/(?P<pk>\d+)/$', login_required(NotaIndEdit.as_view()), name='editar_nota_ind'),
    #Notas Grupales
    url(r'^crear_nota_grup/(?P<id_grupo>\d+)/$', login_required(CrearNotaGrup), name='crear_nota_grup'),
    url(r'^notas_grup', login_required(VerNotasGrup.as_view()), name='notas_grup'),
    url(r'^borrar_nota_grup/(?P<pk>\d+)/$', login_required(NotaGrupDelete.as_view()), name='borrar_nota_grup'),
    url(r'^editar_nota_grup/(?P<pk>\d+)/$', login_required(NotaGrupEdit.as_view()), name='editar_nota_grup'),


]
