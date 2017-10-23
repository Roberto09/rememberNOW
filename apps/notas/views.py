from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.notas.models import Nota_individual, Nota_grupal
from apps.grupos.models import Grupo
from apps.notas.forms import NotaIndividualForm, NotaGrupalForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from apps.grupos.models import Grupo
# Create your views here.


"""NOTAS INDIVIDUALES"""
class CrearNotaInd (CreateView):
	model= Nota_individual
	form_class = NotaIndividualForm
	template_name = 'notas_individuales/crear_notas_ind.html'
	success_url = reverse_lazy('notas:notas_ind')

	def form_valid(self, form):
		form.instance.usuario_nota = self.request.user
		return super(CrearNotaInd, self).form_valid(form)

class VerNotasInd (ListView):
	model=Nota_individual
	template_name = 'notas_individuales/notas_ind.html'
	def get_context_data(self, **kwargs):
		context = super(VerNotasInd, self).get_context_data(**kwargs)
		filtro=self.request.user.pk
		context['Notas']=Nota_individual.objects.filter(usuario_nota=filtro)
		return context

class NotaIndDelete (DeleteView):
	model=Nota_individual
	template_name='notas_individuales/nota_ind_delete.html'
	success_url = reverse_lazy('notas:notas_ind')

class NotaIndEdit (UpdateView):
	model=Nota_individual
	form_class=NotaIndividualForm
	template_name='notas_individuales/crear_notas_ind.html'
	success_url = reverse_lazy('notas:notas_ind')


"""NOTAS GRUPALES"""


def CrearNotaGrup (request, id_grupo):
	grupo=Grupo.objects.get(id=id_grupo)
	usuario_actual=request.user
	form=NotaGrupalForm(request.POST)
	if request.method=='POST':
		if form.is_valid():
			form.instance.creador_nota=usuario_actual
			form.instance.grupo=grupo
			form.save()
		return redirect('notas:notas_ind') #provisional
	return render (request,'notas_grupales/crear_notas_grup.html', {'form':form})

class VerNotasGrup (ListView):
	model=Nota_grupal
	template_name = 'notas_grupales/notas_grup.html'
	def get_context_data(self, **kwargs):
		context = super(VerNotasGrup, self).get_context_data(**kwargs)
		usuario_actual=self.request.user.pk
		Grupos_Usuario=Grupo.objects.filter(integrantes__in=[usuario_actual])
		#Grupos_Usuario=list(Grupos_Usuario)
		context['Notas']=Nota_grupal.objects.filter(grupo__in=list(Grupos_Usuario))
		return context

class NotaGrupDelete (DeleteView):
	model=Nota_grupal
	template_name='notas_individuales/nota_ind_delete.html'
	success_url = reverse_lazy('notas:notas_grup')

class NotaGrupEdit (UpdateView):
	model=Nota_grupal
	form_class=NotaIndividualForm
	template_name='notas_individuales/crear_notas_ind.html'
	success_url = reverse_lazy('notas:notas_grup')


#Como retornar el contexto