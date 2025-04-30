from django.db import models
from django.contrib.auth.models import User
from news.models import Article

class Comment(models.Model):
    """Modelo para comentarios en artículos"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=True)
    upvotes = models.ManyToManyField(User, related_name='comment_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='comment_downvotes', blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"Comment by {self.author.username} on {self.article.title}"

    @property
    def vote_score(self):
        return self.upvotes.count() - self.downvotes.count()