import json

with open('carga/paises.json', encoding='utf8') as json_file:
    paises = json.load(json_file)
    for p in paises['paises']:
        print(p['sigla'] + ' ' + p['nome'])
