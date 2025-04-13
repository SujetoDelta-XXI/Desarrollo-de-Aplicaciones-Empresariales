from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.profile, name='profile'),
    path('reading-lists/', views.reading_list_list, name='reading_list_list'),
    path('reading-lists/new/', views.reading_list_create, name='reading_list_create'),
    path('reading-lists/<int:pk>/', views.reading_list_detail, name='reading_list_detail'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/new/', views.review_create, name='review_create'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
]