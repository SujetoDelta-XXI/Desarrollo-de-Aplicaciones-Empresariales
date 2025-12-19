import requests

def get_pokemon_data(name):
    """Consulta la Poke-Api y devuelve un diccionario con los datos relevantes del Pokémon."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'id': data['id'],
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'base_experience': data['base_experience'],
            'image_url': data['sprites']['front_default']
        }
    return None
