from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from apps.destinos.models import Pais,Continente,Destino
# Create your views here.
# ---------------------AGREGAR ----------------------------
class AgregarContinentes(CreateView):
    model = Continente
    fields =['nombre']
    template_name= 'destinos/agregar_continente.html'
    success_url = reverse_lazy('index')

class AgregarPaises(CreateView):
    model = Pais
    fields =['pais','continente']
    template_name= 'destinos/agregar_pais.html'
    success_url = reverse_lazy('index')

class AgregarDestino(CreateView):
    model = Destino
    fields =['destino','pais']
    template_name= 'destinos/agregar_destino.html'
    success_url = reverse_lazy('index')
