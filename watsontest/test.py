import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

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

#for item in tone_analysis:
 #   if "tones" in item:
  #      print item.get("tones").get("tone_name")

extract_element_from_json(tone_analysis, ["document_tone"]["tones"][0]["tone_name"])
print(json.dumps(tone_analysis, array, indent=2))
