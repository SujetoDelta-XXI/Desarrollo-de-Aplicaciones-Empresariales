from django.db import models
from django.contrib.auth.models import User

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    calendar_id = models.CharField(max_length=200, help_text="ID del calendario en Google Calendar")

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    motivo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.laboratorio.nombre} - {self.fecha_inicio:%d/%m/%Y %H:%M}"
