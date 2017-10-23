from django.shortcuts import render
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario
from django.views.generic import CreateView, ListView
from apps.grupos.models import Grupo
from apps.grupos.forms import GrupoForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class CrearGrupo(CreateView):
	model = Grupo
	form_class = GrupoForm
	template_name = 'grupos/crear_grupos.html'
	success_url = reverse_lazy('notas:notas_ind')

	def get_form(self, form_class=None):
		form = super(CrearGrupo, self).get_form(form_class)
		id_actual_usuario=self.request.user.pk
		actual_usuario=Usuario.objects.get(propiedades_usuario=id_actual_usuario)
		form.fields['integrantes'].queryset = actual_usuario.amigos.all()
		return form

	def post(self,request,*args,**kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		usuario_actual=self.request.user
		if form.is_valid():
			form.instance.Creador_Grupo = usuario_actual
			form.save()
			form.instance.integrantes.add(usuario_actual)
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponse("Algo salio mal, intentalo denuevo")

class VerGrupos(ListView):
	model = Grupo
	template_name = 'grupos/ver_grupos.html'
	def get_context_data(self, **kwargs):
		context = super(VerGrupos, self).get_context_data(**kwargs)
		filtro=self.request.user.pk
		context['Grupos']=Grupo.objects.filter(integrantes__in=[filtro])
		return context

		#module.workflow_set.filter(trigger_roles__in=[self.role], allowed=True)


