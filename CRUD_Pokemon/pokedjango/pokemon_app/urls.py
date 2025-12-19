from django.urls import path
from .views import (
    PokemonCreateView, PokemonListView, PokemonDetailView, PokemonAddView,
    PokemonUpdateView, PokemonDeleteView, home
)

urlpatterns = [
    path('', home.as_view(), name='index'),
    path('pokemon/list', PokemonListView.as_view(), name='pokemon_list'),
    path('pokemon/<int:pk>/', PokemonDetailView.as_view(), name='pokemon_detail'),
    path('create/', PokemonAddView.as_view(), name='pokemon_add'),
    path('update/<int:pk>/', PokemonUpdateView.as_view(), name='pokemon_update'),
    path('delete/<int:pk>/', PokemonDeleteView.as_view(), name='pokemon_delete'),
    path('pokemon_create/', PokemonCreateView.as_view(), name='pokemon_create'),
]
