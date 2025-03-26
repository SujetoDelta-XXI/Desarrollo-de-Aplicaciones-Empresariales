from django.db import models

# Create your models here.

class Usuarios(models.Model):
    Estado = [
        ('casado', 'casado'),
        ('soltero', 'soltero'),
        ('divorciado', 'divorciado'),
    ]
    
    name = models.CharField(max_length=200)
    profesion = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    special_day = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=15,
        choices=Estado,
        default='soltero'
    )
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_date']