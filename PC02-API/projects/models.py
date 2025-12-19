from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    nombre_participante = models.CharField(max_length=100)
    correo = models.EmailField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    asistencia_confirmada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre_participante} - {self.evento.nombre}"

