from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, ReadingHistory, Bookmark, CategorySubscription

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Configuración de administración para perfiles"""
    list_display = ('user', 'display_avatar', 'dark_mode')
    search_fields = ('user__username', 'user__email', 'bio')
    
    def display_avatar(self, obj):
        """Mostrar avatar del usuario"""
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', obj.avatar.url)
        return "Sin avatar"
    
    display_avatar.short_description = "Avatar"

@admin.register(ReadingHistory)
class ReadingHistoryAdmin(admin.ModelAdmin):
    """Configuración de administración para historial de lectura"""
    list_display = ('user', 'article', 'read_at')
    list_filter = ('user', 'read_at')
    search_fields = ('user__username', 'article__title')
    date_hierarchy = 'read_at'

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    """Configuración de administración para marcadores"""
    list_display = ('user', 'article', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'article__title')
    date_hierarchy = 'created_at'

@admin.register(CategorySubscription)
class CategorySubscriptionAdmin(admin.ModelAdmin):
    """Configuración de administración para suscripciones a categorías"""
    list_display = ('user', 'category', 'subscribed_at')
    list_filter = ('category', 'subscribed_at')
    search_fields = ('user__username', 'category__name')
    date_hierarchy = 'subscribed_at'