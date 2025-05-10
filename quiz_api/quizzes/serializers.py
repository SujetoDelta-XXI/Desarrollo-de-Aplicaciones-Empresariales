from rest_framework import serializers
from .models import Quiz, Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "question","text", "is_correct")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id" ,"quiz", "text")


class QuestionDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "quiz", "text", "choices")


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("id", "title", "description", "created_at")


class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuestionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ("id", "title", "description", "created_at", "questions")


class AnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()