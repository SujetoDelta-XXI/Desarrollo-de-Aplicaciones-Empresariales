from django import forms
from django.contrib.auth.models import User
from .models import Profile
from news.models import Category

class UserUpdateForm(forms.ModelForm):
    """Formulario para actualizar información del usuario"""
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    """Formulario para actualizar perfil de usuario"""
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'dark_mode']

class CategorySubscriptionForm(forms.Form):
    """Formulario para gestionar suscripciones a categorías"""
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )