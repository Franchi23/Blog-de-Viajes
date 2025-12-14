from django.contrib import admin
from .models import Contacto

# Register your models here.
admin.site.register(Contacto)

class Contacto(admin.ModelAdmin):
    list_display= ('id','nombre','email','asunto','fecha')
