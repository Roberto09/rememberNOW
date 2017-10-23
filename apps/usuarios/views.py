from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.usuarios.models import Usuario
from apps.usuarios.forms import UsuarioForm, UserDataForm

# Create your views here.
#prueba
def prueba (request):
	return render(request, 'pruebas/prueba.html')

	
class Crear_Usuario (CreateView):
	model=Usuario
	form_class = UsuarioForm
	second_form_class = UserDataForm
	template_name = 'usuarios/register.html'
	success_url = reverse_lazy('login')

	def get_context_data(self, **kwargs):
		context = super(Crear_Usuario,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form']=self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2']=self.second_form_class(self.request.GET)
		return context

	def post(self,request,*args,**kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			usuario = form.save(commit=False)
			usuario.propiedades_usuario = form2.save()
			usuario.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponse("Algo salio mal, intentalo denuevo")

