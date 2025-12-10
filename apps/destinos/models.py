from django.db import models

# Create your models here.
#----------------- CONTINENTE -----------------------------------------
class Continente(models.Model):
    nombre = models.CharField(max_length=50,null=False,unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre',]
        verbose_name_plural = "Continentes"

#----------------- PAIS -----------------------------------------
class Pais(models.Model):
    pais= models.CharField(max_length=70, null=False,unique=True)
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE, related_name='paises')  # con related_name puedo acceder a los países desde un continente: continente.paises.all()

    def __str__(self):
        return self.pais
    
    class Meta:
        ordering = ['pais',]
        verbose_name_plural = "Paises"

#----------------- LUGAR -----------------------------------------
class Destino(models.Model):
    destino = models.CharField(max_length=100, null=False,unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='destinos')  # con related_name puedo acceder a los destino desde un pais: pais.destinos.all()

    def __str__(self):
        return f"{self.destino} - {self.pais}"
    
    class Meta:
        ordering = ['pais','destino',]
        verbose_name_plural = "Destinos"
