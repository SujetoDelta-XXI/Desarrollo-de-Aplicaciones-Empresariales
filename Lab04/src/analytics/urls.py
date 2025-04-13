from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('book-views/', views.book_views, name='book_views'),
    path('author-analytics/', views.author_analytics, name='author_analytics'),
    path('category-analytics/', views.category_analytics, name='category_analytics'),
]
