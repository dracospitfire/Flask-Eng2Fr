import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['qDkjacjuOFb_QbI5aHtJnK4EBMrd5eB5pNNL24U57NAI']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/9aee5273-0a5b-4b02-9e20-fa3bd46feefc']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    #This function takes English text and translates it to French. 
    translation_response = language_translator.translate(text=englishText, model_id='en-fr')
    translation=translation_response.get_result()
    frenchText =translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    #This function takes French text and translates it to English. 
    translation_response = language_translator.translate(text=frenchText, model_id='en-fr')
    translation=translation_response.get_result()
    frenchText =translation['translations'][0]['translation']
    return englishText