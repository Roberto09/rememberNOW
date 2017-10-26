from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario
from apps.amigos.forms import BusquedaUser 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def BuscarAmigos(request, userentry='default'):

	if request.method=='GET':
		usuarios=User.objects.filter(username__contains=userentry)

	if request.method=='POST':
		form = BusquedaUser(request.POST)
		if form.is_valid():
			data= form.cleaned_data
			usuario=data['busqueda_usuario']
			return HttpResponseRedirect(reverse('amigos:buscar_amigos_search', args=(usuario,)))
	else:
		form=BusquedaUser()

	return render(request, "amigos/buscar_amigos.html", {'form':form, 'users':usuarios})

def AgregarAmigos(request, id_usuario):
	amigo=User.objects.get(pk=id_usuario)
	if request.method=='POST':
		actual_user=request.user
		id_actual_usuario=actual_user.pk
		actual_usuario=Usuario.objects.get(propiedades_usuario=id_actual_usuario)
		actual_usuario.amigos.add(amigo)

		actual_amigo=Usuario.objects.get(propiedades_usuario=(amigo.pk))
		actual_amigo.amigos.add(actual_user)

		return redirect('notas:notas_ind')
	return render(request, 'amigos/agregar_amigo.html', {'amigo':amigo})

class ListaAmigos (ListView):
	model=Usuario
	template_name='amigos/amigos.html'
	def get_context_data(self, **kwargs):
	    context = super(ListaAmigos, self).get_context_data(**kwargs)
	    id_actual_usuario=self.request.user.pk
	    actual_usuario=Usuario.objects.get(propiedades_usuario=id_actual_usuario)
	    context['amigos']=actual_usuario.amigos
	    return context






