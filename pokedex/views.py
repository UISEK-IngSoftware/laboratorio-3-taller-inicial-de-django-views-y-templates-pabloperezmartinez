from django.shortcuts import render
from .models import Pokemon

# Create your views here.
def index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})

def pokemon_details(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemon_details.html', {'pokemon': pokemon})