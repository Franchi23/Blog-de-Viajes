from apps.contacto.views import ContactoForm
from . import views
from django.urls import path

app_name = "apps.contacto"

urlpatterns = [
    path('contacto/',views.ContactoForm.as_view(), name='contacto'),
    path('acerca_de/', views.acerca_view, name='acerca_de')
]