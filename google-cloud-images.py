import os
import firebase_admin
import configparser
from firebase_admin import credentials, firestore, storage

localDir = 'icones'
remoteDir = 'champions'

config = configparser.RawConfigParser()
config.read('local.properties')

# Use a service account
cred = credentials.Certificate(config.get('Certificate', 'location'))

firebase_admin.initialize_app(cred, {'storageBucket': config.get('Certificate', 'name')})
db = firestore.client()
bucket = storage.bucket()

for filename in os.listdir(localDir):
    blob = bucket.blob(remoteDir + '/' + filename)
    outfile = localDir + '/' + filename
    with open(outfile, 'rb') as my_file:
        blob.upload_from_file(my_file, content_type='image/png')
