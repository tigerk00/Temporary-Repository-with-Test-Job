from io import BytesIO

import requests
import json
from .models import Pokemon
from django.core import files





def fill_db(s, num):
    for x in range(s, num):
        BASE_URL = 'http://pokeapi.co'
        def query(resource_url):
            url = f"{BASE_URL}{resource_url}{x}/"
            response = requests.get(url)

            if response.status_code == 200:
                return json.loads(response.text)
            return None

        pokemon = query('/api/v2/pokemon/')
        pokemon_species = query(f"/api/v2/pokemon-species/")

        image_url = pokemon['sprites']['other']["official-artwork"]['front_default']
        resp = requests.get(image_url)


        fp = BytesIO()
        fp.write(resp.content)
        file_name = image_url.split("/")[-1]

        Pokemon(name= pokemon['name'],
                id=pokemon['id'],
                weight= pokemon['weight'],
                height= pokemon['height'],
                base_happiness= pokemon_species["base_happiness"],
                capture_rate= pokemon_species["capture_rate"],
                has_gender_differences= pokemon_species["has_gender_differences"],
                is_baby= pokemon_species["is_baby"],
                is_legendary= pokemon_species["is_legendary"],
                is_mythical= pokemon_species["is_mythical"],
                is_playing= False,
                ).image.save(file_name, files.File(fp))





def get_detail_pokemon(name_pk):
    BASE_URL = 'http://pokeapi.co'

    def query(resource_url):
        url = f"{BASE_URL}{resource_url}{name_pk}/"
        response = requests.get(url)

        if response.status_code == 200:
            return json.loads(response.text)
        return None

    pokemon = query('/api/v2/pokemon/')
    pokemon_species = query(f"/api/v2/pokemon-species/")

    return {"id":pokemon['id'],
            "name": pokemon['name'],
            "weight": pokemon['weight'],
            "height": pokemon['height'],
            "image": pokemon['sprites']['other']["official-artwork"]['front_default'],
            "base_happiness": ["base_happiness"],
            "capture_rate": pokemon_species["capture_rate"],
            "has_gender_differences": pokemon_species["has_gender_differences"],
            "is_baby": pokemon_species["is_baby"],
            "is_legendary": pokemon_species["is_legendary"],
            "is_mythical": pokemon_species["is_mythical"],
            }

