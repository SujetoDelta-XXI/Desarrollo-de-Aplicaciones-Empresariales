from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from news.models import Article, Category

class Profile(models.Model):
    """Modelo para perfil de usuario extendido"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    dark_mode = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Crear un perfil automáticamente cuando se crea un usuario"""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Guardar el perfil cuando se guarda el usuario"""
    instance.profile.save()

class ReadingHistory(models.Model):
    """Modelo para registrar el historial de lectura de artículos"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_history')
    article = models.ForeignKey('news.Article', on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-read_at']
        unique_together = ['user', 'article']
    
    def __str__(self):
        return f'{self.user.username} read {self.article.title}'

class Bookmark(models.Model):
    """Modelo para guardar artículos favoritos"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    article = models.ForeignKey('news.Article', on_delete=models.CASCADE, related_name='bookmarked_by')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'article']
    
    def __str__(self):
        return f'{self.user.username} bookmarked {self.article.title}'

class CategorySubscription(models.Model):
    """Modelo para suscripciones a categorías"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_subscriptions')
    category = models.ForeignKey('news.Category', on_delete=models.CASCADE, related_name='subscribers')
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'category']
    
    def __str__(self):
        return f'{self.user.username} subscribed to {self.category.name}'
