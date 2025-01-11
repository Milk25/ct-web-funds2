import requests
import json


api_url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(api_url)
json_data = response.text


# print(f"Abilities and names of Pokemon: {poki_data}")



pokemon_names = ["pikachu", "bulbasaur", "charmander"]
# pokemon_attributes = pokemon_names
def fetch_pokemon_data(pokemon_names):
    # pokemon_names = ["pikachu", "bulbasaur", "charmander"]
    pokemon_list = []
    for pokemon_name in pokemon_names:
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(api_url)
        json_data = response.json()
        name = json_data['name']
        abilities = json_data['abilities']
        weight = json_data['weight']
        print(f"Pokemon:, {name}")
        print(f"Abilities:, {abilities}")
        print(f"Weight:, {weight}")
        new_pokemon = {
            "name": name,
            "abilities": abilities,
            "weight": weight 
        }
        pokemon_list.append(new_pokemon)
         # take weight from pokemon sum all of them and divide by all of them
    pokemon_list_length = len(pokemon_list)
    total_weight = 0
    average_weight = 0
    name = pokemon_names
    
    for pokemon in pokemon_list:
        print(f"pokemon: {pokemon}")
        total_weight = new_pokemon["weight"] / pokemon_list_length
        average_weight += total_weight
        # Find the key of weight 
        # add the pokemon weight value to the total weight 

    average_weight = total_weight / pokemon_list_length
    print(f"Average weight: {average_weight}")
        # Create pokemon object with name, abilities, weight 
        # append the new pokemon object to the pokemon list 
    return pokemon_list

pokemon_list = fetch_pokemon_data(pokemon_names)

