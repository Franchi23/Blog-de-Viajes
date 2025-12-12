from django.urls import path

from apps.viajes.views import AgregarViaje,ActualizarViaje,ListarViajes,EliminarViaje,ordenar_por,listar_viaje_por_destino,leer_viaje,listar_viaje_por_pais

app_name = "apps.viajes"

urlpatterns = [
    path('agregar_viaje/',AgregarViaje.as_view(),name='agregar_viaje'),
    path('actualizar_viaje/<int:pk>', ActualizarViaje.as_view(), name="actualizar_viaje"),
    path("eliminar_viaje/<int:pk>", EliminarViaje.as_view(), name="eliminar_viaje"),
    path("listar_viajes/", ListarViajes.as_view(), name="listar_viajes"),
    path("listar_por_destino/<str:destino>", listar_viaje_por_destino, name="listar_por_destino"),
    path("listar_por_pais/<str:pais>", listar_viaje_por_pais, name="listar_por_pais"),
    path("ordenar_por", ordenar_por , name="ordenar_por"),
    path("viaje/<int:id>", leer_viaje , name = "viaje"),
]
