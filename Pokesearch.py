import requests

url_api="https://pokeapi.co/api/v2/pokemon/"

def main():
    Nombre_pokemon = input("Nombre del pokemon ")
    Url_Nombre_pokemon = url_api + Nombre_pokemon
    Datos_pokemon= get_pokemon_data(Url_Nombre_pokemon)
    print(Datos_pokemon)

def get_pokemon_data(url_pokemon=''):
    Pokemon_data = {
        "id":'',
        "Nombre":'',
        "Tamaño":'',
        "Habilidades":'',
        "Tipo":'',
        "Peso":""
    }
    
    respuesta= requests.get(url_pokemon)
    Datos_pokemon = respuesta.json()
    #nombres en http://jsonviewer.stack.hu/ usando https://pokeapi.co/api/v2/pokemon/charizard
    Pokemon_data ['id'] = Datos_pokemon['id']
    Pokemon_data ['Nombre'] = Datos_pokemon['name']
    Pokemon_data ['Tamaño'] = Datos_pokemon['height']
    Pokemon_data ['Peso'] = Datos_pokemon['weight']
    Pokemon_data ['Habilidades'] = len(Datos_pokemon['abilities'])
    Pokemon_data ['Tipo'] = Datos_pokemon['types']
    
    return Pokemon_data

if __name__ == '__main__':
    main()
