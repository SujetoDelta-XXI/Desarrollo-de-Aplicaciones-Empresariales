from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Comment
from .forms import CommentForm, ReplyForm
from news.models import Article

@login_required
def add_comment(request, article_id):
    """Vista para añadir un comentario a un artículo"""
    article = get_object_or_404(Article, id=article_id, status='published')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            messages.success(request, "¡Tu comentario ha sido publicado!")
            return redirect('news:article_detail', slug=article.slug)
    
    return redirect('news:article_detail', slug=article.slug)

@login_required
def add_reply(request, comment_id):
    """Vista para responder a un comentario existente"""
    parent_comment = get_object_or_404(Comment, id=comment_id, is_approved=True)
    
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.article = parent_comment.article
            reply.author = request.user
            reply.parent = parent_comment
            reply.save()
            messages.success(request, "¡Tu respuesta ha sido publicada!")
    
    return redirect('news:article_detail', slug=parent_comment.article.slug)

@login_required
@require_POST
def vote_comment(request, comment_id, vote_type):
    """Vista para votar a favor o en contra de un comentario"""
    comment = get_object_or_404(Comment, id=comment_id, is_approved=True)
    user = request.user
    
    # Manejar votos positivos
    if vote_type == 'upvote':
        if user in comment.upvotes.all():
            # Quitar voto si ya votó
            comment.upvotes.remove(user)
        else:
            # Añadir voto positivo y quitar voto negativo si existe
            comment.upvotes.add(user)
            comment.downvotes.remove(user)
    
    # Manejar votos negativos
    elif vote_type == 'downvote':
        if user in comment.downvotes.all():
            # Quitar voto si ya votó
            comment.downvotes.remove(user)
        else:
            # Añadir voto negativo y quitar voto positivo si existe
            comment.downvotes.add(user)
            comment.upvotes.remove(user)
    
    # Devolver JSON con la puntuación actualizada para AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'score': comment.vote_score,
            'upvoted': user in comment.upvotes.all(),
            'downvoted': user in comment.downvotes.all()
        })
    
    # Redireccionar a la página del artículo si no es AJAX
    return redirect('news:article_detail', slug=comment.article.slug)