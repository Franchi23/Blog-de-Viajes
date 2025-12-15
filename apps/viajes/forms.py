from datetime import date
from django.forms import DateInput, ModelForm
from apps.viajes.models import Viaje


class ViajeForm(ModelForm):
    model = Viaje
    fields =['titulo','descripcion','imagen','destino','fecha_viaje',]
    widgets ={
        'fecha_viaje': DateInput(attrs = {'type': date}),
    }