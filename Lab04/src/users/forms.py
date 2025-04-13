from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import LibraryUser, BookReview, ReadingList

class LibraryUserCreationForm(UserCreationForm):
    class Meta:
        model = LibraryUser
        fields = ['username', 'email', 'bio', 'profile_image', 'favorite_categories']
        widgets = {
            'favorite_categories': forms.CheckboxSelectMultiple()
        }

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
