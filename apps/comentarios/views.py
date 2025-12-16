from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

from apps.comentarios.forms import ComentarioForm
from apps.comentarios.models import Comentario
from apps.viajes.models import Viaje

# Create your views here.
def agregar_comentario(request):
    form = ComentarioForm(request.Post or None)
    if form.is_valid():
        form.save()
        form =ComentarioForm
    
    template_name = 'comentarios/agregar_comentario.html'
    context = {
        'form' : form
    }
    return render(request,template_name, context)

def listar_comentarios(request):
    comentario = Comentario.objects.all()
    template_name = 'comentarios/listar_comentarios.html'
    context = {
        'comentarios' : comentario
    }
    return render(request,template_name, context)


class ModificarComentario(LoginRequiredMixin, UpdateView):
    model = Comentario
    fields =['comentario']
    template_name = 'comentarios/agregar_comentario.html'
    success_url = reverse_lazy('apps.viajes:listar_viajes')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario = self.request.user)

        return queryset
    
class EliminarComentario(LoginRequiredMixin,DeleteView):
    model = Comentario
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('apps.viajes:listar_viajes')

