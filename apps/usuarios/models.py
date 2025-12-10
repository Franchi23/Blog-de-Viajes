from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.EmailField()
    fecha_nacimiento = models.DateField("Fecha_nacimiento", default='2000-1-1')
    es_colaborador = models.BooleanField("Es_colaborador", default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios', default='usuarios/user_default.png')

    class Meta:
        ordering = ('-nombre',)

    def __str__(self):
        return self.nombre
