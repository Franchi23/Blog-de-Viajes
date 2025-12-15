from pyexpat.errors import messages
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

from apps.usuarios.models import Usuario
from apps.usuarios.forms import RegistroUsuarioForm

# Create your views here.
class RegistrarUsuario(CreateView):
    model= Usuario
    form_class = RegistroUsuarioForm
    template_name ='usuarios/registrar_usuarios.html'
    success_url = reverse_lazy('index')

class LogoutUsuario(LogoutView):
    template_name ='usuarios/cerrar_sesion.html'

    def get_succes_url(self):
        messages.succes(self.request,'Logout Exitoso')

        return reverse('apps.usuarios.iniciar_sesion')
