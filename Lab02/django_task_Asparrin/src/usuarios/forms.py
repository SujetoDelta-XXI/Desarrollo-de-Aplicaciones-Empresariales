from django import forms
from .models import Usuarios

class TaskForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['name', 'profesion', 'special_date', 'estado']
        widgets = {
            'special_date': forms.DateInput(attrs={'type': 'date'}),
            'profesion': forms.Textarea(attrs={'rows': 4}),
        }
