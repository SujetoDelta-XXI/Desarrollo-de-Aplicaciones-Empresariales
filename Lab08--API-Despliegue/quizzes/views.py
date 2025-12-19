from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, Question, Choice
from .serializers import (
    QuizSerializer,
    QuizDetailSerializer,
    QuestionSerializer,
    QuestionDetailSerializer,
    ChoiceSerializer,
    AnswerSerializer,
)


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()

    def get_serializer_class(self):
        return QuizDetailSerializer if self.action == "retrieve" else QuizSerializer

    @action(detail=True, methods=["post"])
    def validate(self, request, pk=None):
        quiz = self.get_object()
        serializer = AnswerSerializer(data=request.data.get("answers", []), many=True)
        serializer.is_valid(raise_exception=True)

        results = []
        for ans in serializer.validated_data:
            q_id, c_id = ans["question_id"], ans["choice_id"]
            try:
                question = Question.objects.get(id=q_id, quiz=quiz)
                choice = Choice.objects.get(id=c_id, question=question)
                results.append(
                    {
                        "question_id": q_id,
                        "correct": choice.is_correct,
                        "correct_choice": (
                            None
                            if choice.is_correct
                            else Choice.objects.filter(
                                question=question, is_correct=True
                            ).first().id
                        ),
                    }
                )
            except (Question.DoesNotExist, Choice.DoesNotExist):
                results.append({"question_id": q_id, "error": "Not found"})

        correct = sum(1 for r in results if r.get("correct"))
        total = len(results)
        return Response(
            {
                "quiz_id": quiz.id,
                "score": f"{correct}/{total}",
                "percentage": int((correct / total) * 100) if total else 0,
                "results": results,
            }
        )


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        return QuestionDetailSerializer if self.action == "retrieve" else QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer