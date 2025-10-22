from django.shortcuts import render


def index(request):
    pokemons = ['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle', 'Charizard']
    return render(request, 'index.html', {
        'pokemons': pokemons
        })
    
def pokemon_details(request, pokemon):
    return render(request, 'pokemon_details.html', {
        'pokemon': pokemon
    })