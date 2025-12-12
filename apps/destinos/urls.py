from django.urls import path

from apps.destinos.views import AgregarContinentes,AgregarDestino,AgregarPaises

app_name = "apps.destinos"

#------------------URLS de DESTINOS
urlpatterns = [
    path('agregar_continente/',AgregarContinentes.as_view(),name='agregar_continente'),
    path('agregar_destino/',AgregarDestino.as_view(),name='agregar_destino'),
    path('agregar_pais/',AgregarPaises.as_view(),name='agregar_pais'),
]