from rest_framework import viewsets
from .models import QuestionStat, QuizActivity
from .serializers import QuestionStatSerializer, QuizActivitySerializer

class QuestionStatViewSet(viewsets.ModelViewSet):
    queryset = QuestionStat.objects.all()
    serializer_class = QuestionStatSerializer

class QuizActivityViewSet(viewsets.ModelViewSet):
    queryset = QuizActivity.objects.all()
    serializer_class = QuizActivitySerializer
