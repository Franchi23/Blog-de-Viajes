from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields =['nombre','apellido','mail','fecha_nacimiento','imagen','username', 'password1', 'password2',]

        @transaction.atomic
        def save(self):
            user = super().save(commit = False)
            user.is_superuser = False
            user.is_staff = False
            user.save()
            return user