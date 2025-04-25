from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('gestor', 'Gestor de Contratos'),
        ('lector', 'Solo Lectura'),
    )
    
    rol = models.CharField(max_length=20, choices=ROLES, default='lector')
    
    def __str__(self):
        return self.username