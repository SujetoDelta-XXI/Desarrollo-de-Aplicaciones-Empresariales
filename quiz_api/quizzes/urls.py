from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet

router = DefaultRouter()
router.register("quizzes", QuizViewSet)
router.register("questions", QuestionViewSet)
router.register("choices", ChoiceViewSet)

urlpatterns = [path("", include(router.urls))]