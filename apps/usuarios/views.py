from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from apps.usuarios.models import Usuario
from apps.usuarios.forms import RegistroUsuarioForm

# Create your views here.
class RegistrarUsuario(CreateView):
    model= Usuario
    form_class = RegistroUsuarioForm
    template_name ='usuarios/registrar_usuarios.html'
    success_url = reverse_lazy('index')
