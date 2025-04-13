from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import LibraryUser, BookReview, ReadingList

class LibraryUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        help_text="Obligatorio. 150 caracteres o menos. Solo letras, números y @/./+/-/_",
    )
      
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput,
        help_text="Ingresa una contraseña.",
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        strip=False,
        help_text="Vuelve a escribir la misma contraseña para confirmar.",
    )

    email = forms.EmailField(
        label="Correo electrónico",
        help_text="Ingresa un correo válido. Se usará para notificaciones."
    )

    class Meta:
        model = LibraryUser
        fields = ['username', 'email', 'bio', 'profile_image', 'favorite_categories']
        widgets = {
            'favorite_categories': forms.CheckboxSelectMultiple()
        }

    def clean_password2(self):
        # Se simplifica la validación (sin validadores estrictos)
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            self.save_m2m()
        return user

class ReadingListForm(forms.ModelForm):
    class Meta:
        model = ReadingList
        fields = ['name', 'description', 'books', 'is_public']
        widgets = {
            'books': forms.CheckboxSelectMultiple(),
        }

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['book', 'rating', 'comment']
