from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from apps.comentarios.forms import ComentarioForm
from apps.destinos.models import Pais,Destino,Continente
from apps.viajes.models import Viaje
from apps.comentarios.models import Comentario

# Create your views here.
class AgregarViaje(CreateView):
    model = Viaje
    fields =['titulo','descripcion','imagen','destino','fecha_viaje',]
    template_name= 'viajes/agregar_viaje.html'
    success_url = reverse_lazy('index')

class ActualizarViaje(UpdateView):
    model = Viaje
    fields =['titulo','descripcion','imagen','destino','fecha_viaje',]
    template_name= 'viajes/agregar_viaje.html'
    success_url = reverse_lazy('index')

class EliminarViaje(DeleteView):
    model = Viaje
    template_name= 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')

class ListarViajes(ListView):
    model = Viaje
    template_name= 'viajes/listar_viajes.html'
    context_object_name ="viajes"
    paginate_by = 4

    def get_context_data(self):
        context = super().get_context_data()
        destino = Destino.objects.all()
        context["destino"] = destino
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains = query )

        return queryset.order_by('titulo')

def listar_por_destino(request, destino):
    destino_filtrado= Destino.objects.filter(destino = destino)
    viaje = Viaje.objects.filter(destino = destino_filtrado[0].id ).order_by('fecha_viaje')
    destino = Destino.objects.all()
    template_name = "viajes/listar_viajes.html"
    context = {
        'viaje' : viaje,
        'destino' : destino
    }
    return render(request, template_name, context)

#Ver esto que es un filtro de un filtro ????
#Busco los destinos del pais filtrado y los devuelvo?????
def listar_por_pais(request, pais):
    pais_filtrado= Pais.objects.filter(pais = pais)
    destino_filtrado = Destino.objects.filter(pais = pais_filtrado[0].index)
    viaje = Viaje.objects.filter(destino = destino_filtrado[0].id ).order_by('fecha_viaje')
    pais = Pais.objects.all()
    destinos = Destino.objects.all()
    template_name = "viajes/listar_viajes.html"
    context = {
        'viaje' : viaje,
        'pais' : pais,
        'destino': destinos
    }
    return render(request, template_name, context)

def ordenar_por(request):
    orden = request.GET.get('orden','')

    if orden == "fecha":
        viajes = Viaje.objects.order_by('publicacion')
    elif orden == "titulo":
        viajes = Viaje.objects.order_by('titulo')
    elif orden == "destino":
        viajes = Viaje.objects.order_by('destino')
    else:
        viajes = Viaje.objects.all()

    context ={
        "viajes" : viajes 
    }
    template_name = "viajes/listar_viajes.html"

    return render(request, template_name, context)

def leer_viaje(request, id):
     viaje = Viaje.objects.get(id = id)
     comentario = Comentario.objects.filter(viaje = id)
     form = ComentarioForm(request.POST)

     if form.is_valid():
         if request.user.is_authenticated:
             aux = form.save(commit=False)
             aux.viaje = viaje
             aux.usuario = request.user
             aux.save()
             form = ComentarioForm()
         else:
             return redirect("apps.usuarios:iniciar_sesion")
     template_name = "viajes/viajes.html"
     context = {
         "viaje" : viaje,
         "form" : form,
         "comentario" : comentario
     }
     return render(request, template_name, context)