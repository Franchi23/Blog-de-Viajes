from django.urls import path

from apps.destinos.views import AgregarContinentes,AgregarDestino,AgregarPaises,ListarDestinos,ListarPais,ListarContinentes

app_name = "apps.destinos"

#------------------URLS de DESTINOS
urlpatterns = [
    path('agregar_continente/',AgregarContinentes.as_view(),name='agregar_continente'),
    path('agregar_destino/',AgregarDestino.as_view(),name='agregar_destino'),
    path('agregar_pais/',AgregarPaises.as_view(),name='agregar_pais'),
    path('listar_pais/', ListarPais.as_view(), name='listar_pais'),
    path('listar_destinos/', ListarDestinos.as_view(), name='listar_destinos'),
    path('listar_continentes/', ListarContinentes.as_view(), name='listar_continentes'),
]