from django.contrib import admin
from apps.destinos.models import Destino, Continente,Pais

# Register your models here.
admin.site.register(Destino)
admin.site.register(Continente)
admin.site.register(Pais)
