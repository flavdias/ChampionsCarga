import json
import firebase_admin
import configparser
from firebase_admin import credentials
from firebase_admin import firestore

config = configparser.RawConfigParser()
config.read('local.properties')

# Use a service account
cred = credentials.Certificate(config.get('Certificate', 'location'))
firebase_admin.initialize_app(cred)

with open('carga/paises.json', encoding='utf8') as json_file:
    paises = json.load(json_file)

with open('carga/times.json', encoding='utf8') as json_file:
    times = json.load(json_file)

with open('carga/potes.json', encoding='utf8') as json_file:
    potes = json.load(json_file)


db = firestore.client()

for x in paises['paises']:
    doc_ref = db.collection('paises').document(x['sigla'])
    doc_ref.set({
        u'sigla': x['sigla'],
        u'nome': x['nome']
    })

for y in times['times']:
    doc_ref = db.collection('times').document(y['sigla'])
    doc_ref.set({
        u'sigla': y['sigla'],
        u'nome': y['nome'],
        u'pais': y['pais'],
        u'icone': y['icone']
    })

for z in potes['potes']:
    titulo = z['sigla'] + "-" + str(z['pote']) + "-" + str(z['ano'])
    doc_ref = db.collection('potes').document(titulo)
    doc_ref.set({
        u'sigla': z['sigla'],
        u'pote': z['pote'],
        u'ano': z['ano']
    })
