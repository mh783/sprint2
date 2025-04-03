from django.db import models

class Examen(models.Model):
    TIPO_CHOICES = [
        ('EEG', 'EEG'),
        ('MRI', 'MRI'),
        ('miRNA', 'miRNA'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha = models.DateField(auto_now_add=True)
    archivo = models.CharField(max_length=255)  # Simula ruta o nombre de archivo
    estado = models.CharField(max_length=50, default='pendiente')
    resumen_resultados = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    datos_adicionales = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.tipo} - {self.fecha}"