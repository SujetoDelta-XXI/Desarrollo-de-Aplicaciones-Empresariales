from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import inlineformset_factory
from django.db import transaction
from .models import Exam, Question, Choice
from .forms import ExamForm, QuestionForm, ChoiceFormSet
from .forms import ChoiceForm 


def exam_list(request):
    """Vista para listar todos los exámenes"""
    exams = Exam.objects.all().order_by('-created_date')
    return render(request, 'quiz/exam_list.html', {'exams': exams})

def exam_detail(request, exam_id):
    """Vista para mostrar el detalle de un examen con sus preguntas"""
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all().prefetch_related('choices')
    return render(request, 'quiz/exam_detail.html', {'exam': exam, 'questions': questions})

def exam_create(request):
    """Vista para crear un nuevo examen"""
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(request, 'Examen creado correctamente.')
            return redirect('question_create', exam_id=exam.id)
    else:
        form = ExamForm()
    
    return render(request, 'quiz/exam_form.html', {'form': form})

def question_create(request, exam_id):
    """Vista para añadir preguntas a un examen"""
    exam = get_object_or_404(Exam, id=exam_id)
    
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        
        if question_form.is_valid():
            with transaction.atomic():
                # Guardar la pregunta
                question = question_form.save(commit=False)
                question.exam = exam
                question.save()
                
                # Procesar el formset para las opciones
                formset = ChoiceFormSet(request.POST, instance=question)
                if formset.is_valid():
                    formset.save()
                    
                    # Verificar que solo una opción sea marcada como correcta
                    correct_count = question.choices.filter(is_correct=True).count()
                    if correct_count != 1:
                        messages.warning(request, 'Debe haber exactamente una respuesta correcta.')
                    else:
                        messages.success(request, 'Pregunta añadida correctamente.')
                        
                    # Decidir a dónde redirigir
                    if 'add_another' in request.POST:
                        return redirect('question_create', exam_id=exam.id)
                    else:
                        return redirect('exam_detail', exam_id=exam.id)
    else:
        question_form = QuestionForm()
        formset = ChoiceFormSet()
    
    return render(request, 'quiz/question_form.html', {
        'exam': exam,
        'question_form': question_form,
        'formset': formset,
    })

def exam_play(request, exam_id):
    """Vista para jugar el examen"""
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all().prefetch_related('choices')
    # Aquí puedes agregar la lógica para mostrar una interfaz interactiva del examen.
    return render(request, 'quiz/exam_play.html', {'exam': exam, 'questions': questions})

def question_update(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    exam = question.exam
    
    ChoiceFormSet = inlineformset_factory(Question, Choice, form=ChoiceForm, extra=0, can_delete=True)  # `extra=0` evita agregar campos adicionales

    if request.method == 'POST':
        question_form = QuestionForm(request.POST, instance=question)
        formset = ChoiceFormSet(request.POST, instance=question)
        
        if question_form.is_valid() and formset.is_valid():
            with transaction.atomic():
                question_form.save()
                formset.save()
                
                correct_count = question.choices.filter(is_correct=True).count()
                if correct_count != 1:
                    messages.warning(request, 'Debe haber exactamente una respuesta correcta.')
                else:
                    messages.success(request, 'Pregunta actualizada correctamente.')
                return redirect('exam_detail', exam_id=exam.id)
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        question_form = QuestionForm(instance=question)
        formset = ChoiceFormSet(instance=question)  # Se mostrarán solo las alternativas existentes

    context = {
        'exam': exam,
        'question_form': question_form,
        'formset': formset,
    }
    return render(request, 'quiz/exam_update.html', context)


def question_delete(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    exam = question.exam

    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Pregunta eliminada correctamente.')
        return redirect('exam_detail', exam_id=exam.id)
    else:
        messages.error(request, 'Método no permitido para eliminar la pregunta.')
        return redirect('exam_detail', exam_id=exam.id)
