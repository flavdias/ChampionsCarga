import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('C:/Users/flavi/Documents/service-account-file.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'potes').document(u'MAD-1-2020')
doc_ref.set({"sigla":"MAD", "pote": 1, "ano": "2020"})
