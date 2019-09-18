import firebase_admin
import configparser
from firebase_admin import credentials
from firebase_admin import firestore

config = configparser.RawConfigParser()
config.read('local.properties')

# Use a service account
cred = credentials.Certificate(config.get('Certificate', 'location'))
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'potes').document(u'MAD-1-2020')
doc_ref.set({"sigla":"MAD", "pote": 1, "ano": "2020"})
