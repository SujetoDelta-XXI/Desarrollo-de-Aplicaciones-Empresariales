from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, SerieViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'series', SerieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
