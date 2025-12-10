from django.db import models

from apps.destinos.models import Destino

# Create your models here.
class Viaje(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()
    imagen = models.ImageField(null=True, blank=True, upload_to='viajes', default='viajes/default.png')
    destino = models.ForeignKey(Destino, on_delete=models.SET_NULL, null=True)
    fecha_viaje = models.DateTimeField('Fecha Viaje',auto_now_add=True)
    publicacion = models.DateTimeField('Fecha Publicacion',blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['titulo','destino','-fecha_viaje']
        verbose_name_plural = "Viajes"
