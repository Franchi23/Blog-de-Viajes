from django.urls import path

from apps.comentarios.views import EliminarComentario, ModificarComentario, agregar_comentario, listar_comentarios

app_name = "apps.comentarios"

urlpatterns = [
    path('agregar_comentario/',agregar_comentario,name ='agregar_comentario'),
    path('listar_comentarios/',listar_comentarios,name ='comentarios'),
    path('modificar_comentario/<int:pk>',ModificarComentario.as_view(),name ='modificar_comentario'),
    path('eliminar_comentario/<int:pk>',EliminarComentario.as_view(),name ='eliminar_comentario'),
]
