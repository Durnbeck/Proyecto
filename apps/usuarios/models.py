from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(AbstractUser):
    #imagen de perfil de usuario
    imagen = models.ImageField(upload_to='usuarios', default='default-user.png')
    
    USUARIO_COLABORADOR = 'Colaborador'
    USUARIO_VISITANTE = 'Visitante'
    USUARIO_MIEMBRO = 'Miembro'
    USUARIO_SUPER = 'Superusuario'

    TIPOS_DE_USUARIO = [
        (USUARIO_COLABORADOR, 'Colaborador'),
        (USUARIO_VISITANTE, 'Visitante'),
        (USUARIO_MIEMBRO, 'Miembro'),
        (USUARIO_SUPER, 'Superusuario'),
    ]

    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_DE_USUARIO, default=USUARIO_MIEMBRO)

    def __str__(self):
        return self.username

# Señal para asignar el tipo de usuario "Superusuario" cuando se crea un superusuario
@receiver(post_save, sender=Usuario)
def asignar_tipo_usuario(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        instance.tipo_usuario = Usuario.USUARIO_SUPER
        instance.save()