from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import Comment

@receiver(post_save, sender=Comment)
def send_notification_email(sender, instance, created, **kwargs):
    """Envía un email de notificación cuando se responde a un comentario"""
    if created and instance.parent:
        # Solo se envía la notificación si es una respuesta a otro comentario
        parent_author = instance.parent.author
        
        # No enviar si el usuario se responde a sí mismo
        if parent_author == instance.author:
            return
            
        article = instance.article
        article_url = reverse('news:article_detail', kwargs={'slug': article.slug})
        full_url = f"{settings.SITE_URL}{article_url}#comment-{instance.id}"
        
        subject = f"Alguien ha respondido a tu comentario en '{article.title}'"
        message = f"""
            Hola {parent_author.username},
            
            {instance.author.username} ha respondido a tu comentario en el artículo "{article.title}":
            
            "{instance.content}"
            
            Puedes ver la respuesta aquí: {full_url}
            
            Saludos,
            El equipo de Django News Portal
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [parent_author.email],
            fail_silently=True,
        )