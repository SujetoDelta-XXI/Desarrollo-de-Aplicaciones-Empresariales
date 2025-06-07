from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, ProxiedQuizViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'proxied-quizzes', ProxiedQuizViewSet, basename='proxied-quiz')

urlpatterns = [path('', include(router.urls))]