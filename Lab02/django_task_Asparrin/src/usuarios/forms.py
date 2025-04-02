from django import forms
from .models import Usuarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['name', 'profesion', 'special_day', 'estado']
        widgets = {
            'special_day': forms.DateInput(attrs={'type': 'date'}),
            'profesion': forms.Textarea(attrs={'rows': 4}),
        }
