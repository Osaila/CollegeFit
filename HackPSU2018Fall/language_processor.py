import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "/home/osaila/Documents/HackPSU2018Fall/auth.json"
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six

client = language.LanguageServiceClient()

text = open("school_data.txt","r")
text_in = text.read().decode("utf-8").encode("utf-8")

document = types.Document(
    content=text_in,
    type=enums.Document.Type.PLAIN_TEXT)

# Detect and send native Python encoding to receive correct word offsets.

result = client.analyze_entity_sentiment(document)

for entity in result.entities:
    print('Name: "{}"'.format(entity.name.encode("utf-8")))
    print(u'Salience: {}'.format(entity.salience))
    print(u'Sentiment {}'.format(entity.sentiment))
