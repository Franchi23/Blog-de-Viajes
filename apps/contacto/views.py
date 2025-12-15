from django.shortcuts import render
from .forms import ContactoForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.contacto.models import Contacto

# Create your views here.
class ContactoForm(CreateView):
    model = Contacto
    fields =['nombre','emial','asunto','mensaje','fecha',]
    template_name='contacto/contacto.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reques'] = self.request
        return context

    def form_valid(self,form):
        messages.success(self.request,'Consulta Enviada')
        return super().form_valid(form)

def acerca_view(request):
    return render(request, 'contacto/acerca_de.html')