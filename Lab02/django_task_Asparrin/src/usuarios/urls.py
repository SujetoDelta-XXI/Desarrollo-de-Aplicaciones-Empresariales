from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuario_list, name='usuario_list'),
    path('usuario/new/', views.usuario_create, name='usuario_create'),
    path('usuario/<int:pk>/edit/', views.usuario_update, name='usuario_update'),
    path('usuario/<int:pk>/delete/', views.usuario_delete, name='usuario_delete'),
]
