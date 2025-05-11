from rest_framework import serializers
from .models import QuestionStat, QuizActivity

class QuestionStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionStat
        fields = ['id', 'question', 'attempts', 'correct_attempts', 'success_rate']

class QuizActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizActivity
        fields = ['id', 'quiz', 'date', 'views', 'starts', 'completions']
