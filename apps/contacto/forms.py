from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        models = Contacto
        fields =['nombre','email','asunto','mensaje','fecha']