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

#-------------------------------LISTAR -----------------------------------------
class ListarDestinos(ListView):
    model = Destino
    template_name= 'destinos/listar_destinos.html'
    context_object_name ="destinos"
    paginate_by = 4

    def get_context_data(self):
        context = super().get_context_data()
        pais = Pais.objects.all()
        context["pais"] = pais
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(destino__icontains = query )

        return queryset.order_by('destino')
    
class ListarPais(ListView):
    model = Pais
    template_name= 'destinos/listar_paises.html'
    context_object_name ="paises"
    paginate_by = 4

    def get_context_data(self):
        context = super().get_context_data()
        continente = Continente.objects.all()
        context["continente"] = continente
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(pais__icontains = query )

        return queryset.order_by('pais')

class ListarContinentes(ListView):
    model = Continente
    template_name= 'destinos/listar_continentes.html'
    context_object_name ="continentes"

    def get_context_data(self):
        context = super().get_context_data()
        continente = Continente.objects.all()
        context["continente"] = continente
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(nombre__icontains = query )

        return queryset.order_by('nombre')

