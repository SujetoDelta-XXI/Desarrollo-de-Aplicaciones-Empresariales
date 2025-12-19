from django.db import models

class Actividad(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
