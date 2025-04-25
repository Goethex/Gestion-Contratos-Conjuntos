from django.db import models
from django.conf import settings
from django.utils import timezone

class Contrato(models.Model):
    ESTADOS_CONTRATO = [
        ('vigente', 'Vigente'),
        ('vencido', 'Vencido'),
        ('no_iniciado', 'No Iniciado'),
    ]

    TIPOS_CONTRATO = (
        ('mantenimiento', 'Mantenimiento'),
        ('servicio', 'Servicio'),
        ('obra', 'Obra'),
        ('suministro', 'Suministro'),
        ('otro', 'Otro'),
    )
    
    tipo = models.CharField(max_length=50, choices=TIPOS_CONTRATO)
    titulo = models.CharField(max_length=200)
    parte_a = models.CharField(max_length=200, help_text="Primera parte del contrato (ej. Conjunto Residencial)")
    parte_b = models.CharField(max_length=200, help_text="Segunda parte del contrato (ej. Proveedor)")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contratos_creados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_CONTRATO, default='no_iniciado')
    
    def __str__(self):
        return f"{self.titulo} - {self.get_tipo_display()}"
    
    def actualizar_estado(self):
        """Actualiza el estado del contrato basado en las fechas."""
        hoy = timezone.now().date()
        if self.fecha_inicio > hoy:
            self.estado = 'no_iniciado'
        elif self.fecha_inicio <= hoy <= self.fecha_fin:
            self.estado = 'vigente'
        else:
            self.estado = 'vencido'
        self.save()

class ArchivoAdjunto(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='adjuntos')
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='contratos/adjuntos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class HistorialContrato(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='historial')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion_cambio = models.TextField()
    
    def __str__(self):
        return f"Modificación por {self.usuario.username} el {self.fecha.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        ordering = ['-fecha']