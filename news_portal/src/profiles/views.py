from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Profile, ReadingHistory, Bookmark, CategorySubscription
from .forms import UserUpdateForm, ProfileUpdateForm, CategorySubscriptionForm
from news.models import Article, Category

@login_required
def profile(request):
    """Vista para ver el perfil del usuario"""
    user = request.user
    bookmarks = Bookmark.objects.filter(user=user)
    reading_history = ReadingHistory.objects.filter(user=user)[:10]
    subscriptions = CategorySubscription.objects.filter(user=user)
    
    context = {
        'user': user,
        'bookmarks': bookmarks,
        'reading_history': reading_history,
        'subscriptions': subscriptions,
    }
    return render(request, 'profiles/profile.html', context)

@login_required
def edit_profile(request):
    """Vista para editar el perfil del usuario"""
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado!')
            return redirect('profiles:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'profiles/edit_profile.html', context)

@login_required
def reading_history_view(request):
    """Vista para ver el historial de lectura"""
    reading_history = ReadingHistory.objects.filter(user=request.user)
    paginator = Paginator(reading_history, 10)  # 10 artículos por página
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'profiles/reading_history.html', {'page_obj': page_obj})

@login_required
def bookmarks_view(request):
    """Vista para ver los marcadores guardados"""
    bookmarks = Bookmark.objects.filter(user=request.user)
    paginator = Paginator(bookmarks, 10)  # 10 artículos por página
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'profiles/bookmarks.html', {'page_obj': page_obj})

@login_required
def add_bookmark(request, article_id):
    """Vista para añadir un artículo a marcadores"""
    article = get_object_or_404(Article, id=article_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, article=article)
    
    if created:
        messages.success(request, f'Artículo "{article.title}" añadido a marcadores.')
    else:
        messages.info(request, f'Este artículo ya estaba en tus marcadores.')
    
    # Si es una petición AJAX, devolver respuesta JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'created': created})
    
    # De lo contrario, redirigir de vuelta a la página del artículo
    return redirect('news:article_detail', slug=article.slug)

@login_required
def remove_bookmark(request, bookmark_id):
    """Vista para eliminar un artículo de marcadores"""
    bookmark = get_object_or_404(Bookmark, id=bookmark_id, user=request.user)
    article_title = bookmark.article.title
    bookmark.delete()
    
    messages.success(request, f'Artículo "{article_title}" eliminado de marcadores.')
    
    # Si es una petición AJAX, devolver respuesta JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    # Redirigir a la página de marcadores
    return redirect('profiles:bookmarks')

@login_required
def manage_subscriptions(request):
    """Vista para gestionar suscripciones a categorías"""
    user = request.user
    user_subscriptions = CategorySubscription.objects.filter(user=user).values_list('category_id', flat=True)
    
    if request.method == 'POST':
        form = CategorySubscriptionForm(request.POST)
        if form.is_valid():
            selected_categories = form.cleaned_data['categories']
            
            # Eliminar suscripciones existentes
            CategorySubscription.objects.filter(user=user).delete()
            
            # Crear nuevas suscripciones
            for category in selected_categories:
                CategorySubscription.objects.create(user=user, category=category)
            
            messages.success(request, 'Tus suscripciones han sido actualizadas.')
            return redirect('profiles:profile')
    else:
        form = CategorySubscriptionForm(initial={'categories': user_subscriptions})
    
    return render(request, 'profiles/manage_subscriptions.html', {'form': form})

@login_required
def toggle_dark_mode(request):
    """Vista para alternar el modo oscuro/claro"""
    if request.method == 'POST':
        profile = request.user.profile
        profile.dark_mode = not profile.dark_mode
        profile.save()
        
        # Si es una petición AJAX, devolver respuesta JSON
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success', 'dark_mode': profile.dark_mode})
    
    # Redirigir de vuelta a la página anterior
    return redirect(request.META.get('HTTP_REFERER', 'profiles:profile'))

def record_article_view(request, article_id):
    """Registrar la lectura de un artículo en el historial"""
    if request.user.is_authenticated:
        article = get_object_or_404(Article, id=article_id)
        ReadingHistory.objects.get_or_create(user=request.user, article=article)
    
    # Si es una petición AJAX, devolver respuesta JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    # De lo contrario, no hacer nada visible
    return JsonResponse({'status': 'success'})