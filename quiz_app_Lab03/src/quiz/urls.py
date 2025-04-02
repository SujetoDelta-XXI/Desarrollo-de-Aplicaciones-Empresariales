from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('exam/create/', views.exam_create, name='exam_create'),
    path('exam/<int:exam_id>/question/add/', views.question_create, name='question_create'),
    path('exam/<int:exam_id>/play/', views.exam_play, name='exam_play'),
    path('question/<int:question_id>/update/', views.question_update, name='question_update'),
    path('question/<int:question_id>/delete/', views.question_delete, name='question_delete'),
]
