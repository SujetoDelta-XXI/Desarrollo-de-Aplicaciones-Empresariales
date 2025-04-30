from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Formulario para crear comentarios"""
    content = forms.CharField(
        label="Comentario",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Escribe tu comentario aquí...',
            'class': 'comment-form__input'
        })
    )

    class Meta:
        model = Comment
        fields = ['content']

class ReplyForm(forms.ModelForm):
    """Formulario para responder a comentarios"""
    content = forms.CharField(
        label="Respuesta",
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Escribe tu respuesta aquí...',
            'class': 'reply-form__input'
        })
    )

    class Meta:
        model = Comment
        fields = ['content']