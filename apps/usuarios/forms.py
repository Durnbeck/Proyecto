from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)

    # Agregar el campo de selección para el tipo de usuario
    TIPOS_DE_USUARIO = [
        (Usuario.USUARIO_COLABORADOR, 'Colaborador'),
        (Usuario.USUARIO_VISITANTE, 'Visitante'),
        (Usuario.USUARIO_MIEMBRO, 'Miembro'),
        (Usuario.USUARIO_SUPER, 'Superusuario'),
    ]
    tipo_usuario = forms.ChoiceField(choices=TIPOS_DE_USUARIO, initial=Usuario.USUARIO_MIEMBRO)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            # Agregar el campo 'tipo_usuario' al formulario
        ]