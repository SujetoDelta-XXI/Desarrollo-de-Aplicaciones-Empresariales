from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Configuración de administración para comentarios"""
    list_display = ('author', 'article', 'created_date', 'is_approved', 'parent', 'vote_score')
    list_filter = ('is_approved', 'created_date')
    search_fields = ('content', 'author__username', 'article__title')
    actions = ['approve_comments', 'disapprove_comments']

    def vote_score(self, obj):
        return obj.vote_score
    vote_score.short_description = "Puntuación"

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Aprobar comentarios seleccionados"

    def disapprove_comments(self, request, queryset):
        queryset.update(is_approved=False)
    disapprove_comments.short_description = "Desaprobar comentarios seleccionados"