from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    base_experience = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name.capitalize()
