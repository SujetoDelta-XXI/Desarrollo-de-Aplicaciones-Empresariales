from django.shortcuts import render
from .models import BookView, CategoryAnalytics, AuthorAnalytics
from library.models import Book

def dashboard(request):
    context = {
        'total_views': BookView.objects.count(),
        'top_books': Book.objects.order_by('-views__id')[:5],
        'top_authors': AuthorAnalytics.objects.order_by('-total_views')[:5],
        'category_stats': CategoryAnalytics.objects.order_by('-popularity_score')[:5],
    }
    return render(request, 'analytics/dashboard.html', context)

def book_views(request):
    views = BookView.objects.select_related('book', 'user').order_by('-timestamp')
    return render(request, 'analytics/book_views.html', {'views': views})

def author_analytics(request):
    authors = AuthorAnalytics.objects.select_related('author').order_by('-total_views')
    return render(request, 'analytics/author_analytics.html', {'authors': authors})

def category_analytics(request):
    categories = CategoryAnalytics.objects.select_related('category').order_by('-popularity_score')
    return render(request, 'analytics/category_analytics.html', {'categories': categories})
