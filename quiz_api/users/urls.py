from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, QuizAttemptViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'attempts', QuizAttemptViewSet)

urlpatterns = router.urls