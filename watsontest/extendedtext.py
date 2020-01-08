import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas.io.json import json_normalize
#from scrape import nextPage
from random import seed
from random import randint
from random import shuffle

seed(1)

authenticator = IAMAuthenticator('4VAC4EecGDVM_t3BvRFvdd-dmwDIdpkbnWffTrhoQKZI')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com')

text = 'Team, I know that times are tough! Product '\
       'sales have been disappointing for the past three '\
        'quarters. We have a competitive product, but we '\
        'need to do a better job of selling it!'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()

for j in range(1):
    value = randint(0, 2)
    print(value)
    myData = tone_analysis['document_tone']['tones'][j]['tone_name']    
    print (myData)
    

#mydata = json_normalize(tone_analysis['document_tone'])
#mydata.head(3)
#print(mydata)

#tones_data = json_normalize(data=tone_analysis['document_tone'], record_path='tones')
#tones_data.head(3)
#print(tones_data)

