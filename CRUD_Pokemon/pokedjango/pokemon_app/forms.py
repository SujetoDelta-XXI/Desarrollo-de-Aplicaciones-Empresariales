from django import forms
from .models import Pokemon


class PokemonForm(forms.Form):
    name = forms.CharField(label='Nombre del Pokémon', max_length=100)

class PokemonManualForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'height', 'weight', 'base_experience', 'image_url']
        labels = {
            'name': 'Nombre del Pokémon',
            'height': 'Altura (en metros)',
            'weight': 'Peso (en kg)',
            'base_experience': 'Experiencia base',
            'image_url': 'URL de la imagen'
        }
