from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import PokemonManualForm
from .models import Pokemon
from .forms import PokemonForm
from .utils import get_pokemon_data
from django.contrib import messages

class home(View):
    template_name = 'home.html'
    def get(self, request):
        return render(request, 'home.html')

# Vista para listar los Pokémon registrados
class PokemonListView(ListView):
    model = Pokemon
    template_name = 'pokemon_app/pokemon_list.html'
    context_object_name = 'pokemons'

# Vista para ver los detalles de un Pokémon
class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = 'pokemon_app/pokemon_detail.html'
    context_object_name = 'pokemon'

class PokemonCreateView(View):
    template_name = 'pokemon_app/pokemon_create.html'
    
    def get(self, request):
        form = PokemonManualForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = PokemonManualForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Pokémon creado correctamente!")
            return redirect('pokemon_list')  # Asegúrate que este nombre concuerde con tu URL para listar pokémon
        return render(request, self.template_name, {'form': form})

# Vista para crear un Pokémon consultando la Poke-Api
class PokemonAddView(View):
    template_name = 'pokemon_app/pokemon_form.html'
    
    def get(self, request):
        form = PokemonForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = PokemonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            data = get_pokemon_data(name)
            if data:
                # Se evita duplicar datos verificando si ya existe
                pokemon, created = Pokemon.objects.get_or_create(
                    name=data['name'],
                    defaults={
                        'height': data['height'],
                        'weight': data['weight'],
                        'base_experience': data['base_experience'],
                        'image_url': data['image_url'],
                    }
                )
                if created:
                    messages.success(request, f"¡Pokémon {pokemon.name.capitalize()} creado exitosamente!")
                else:
                    messages.info(request, f"El Pokémon {pokemon.name.capitalize()} ya existe en la base de datos.")
                return redirect('pokemon_list')
            else:
                form.add_error('name', 'No se encontró un Pokémon con ese nombre.')
        return render(request, self.template_name, {'form': form})

# Vista para actualizar un Pokémon (se actualizan los campos manualmente, sin consultar la API)
class PokemonUpdateView(UpdateView):
    model = Pokemon
    fields = ['name', 'height', 'weight', 'base_experience', 'image_url']
    template_name = 'pokemon_app/pokemon_form.html'
    success_url = reverse_lazy('pokemon_list')

# Vista para eliminar un Pokémon
class PokemonDeleteView(DeleteView):
    model = Pokemon
    template_name = 'pokemon_app/pokemon_delete.html'
    success_url = reverse_lazy('pokemon_list')

