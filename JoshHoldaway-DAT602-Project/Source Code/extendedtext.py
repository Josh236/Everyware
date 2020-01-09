import json
#from quotes.json import text
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas.io.json import json_normalize
#from scrape import nextPage
from random import seed
from random import randint
from random import shuffle
import random

random.seed()

jsonRData = 'blah'

authenticator = IAMAuthenticator('4VAC4EecGDVM_t3BvRFvdd-dmwDIdpkbnWffTrhoQKZI')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

with open('quotes.json') as json_file:
    jsonData = json_file.read()

obj = json.loads(jsonData)
for i in range(1):
    jsonVal = random.randint(1,11)
    print(jsonVal)
    jsonRData = (obj[jsonVal]['text'])
    print(jsonRData)



tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com')

text = jsonRData

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()

#for j in range(1):
value = randint(0, 1)
print(value)
myData = tone_analysis['document_tone']['tones'][0]['tone_name']
print (myData)
    

#mydata = json_normalize(tone_analysis['document_tone'])
#mydata.head(3)
#print(mydata)

#tones_data = json_normalize(data=tone_analysis['document_tone'], record_path='tones')
#tones_data.head(3)
#print(tones_data)

