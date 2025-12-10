from django.db import models
from apps.usuarios.models import Usuario
from apps.viajes.models import Viajes

# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    viaje = models.ForeignKey(Viajes, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario
    
    class Meta:
        ordering = ["-fecha",]