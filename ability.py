import json,requests

def ability(pokemon):

    abilities = [] #To store abilities 
    
    url = 'https://pokeapi.co/api/v2/pokemon/'+pokemon 
    res = requests.get(url)
    detail = res.json() # to get details in list
    
    #appending abilities to the list
    for i in detail['abilities']:
        abilities.append(i['ability']['name'])
        
    return abilities
