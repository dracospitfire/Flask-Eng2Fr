"""Modules for Watson Service"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()


def english_2_french(english_text):
    """This function takes English text and translates it to French."""
    apikey = os.environ['apikey']
    url = os.environ['url']
    VERSION='2018-05-01'
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version = VERSION, authenticator = authenticator)
    language_translator.set_service_url(url)
    translation_response = language_translator.translate(text = english_text, model_id = 'en-fr')
    translation = translation_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_2_english(french_text):
    """This function takes French text and translates it to English."""
    translation_response = language_translator.translate(text=french_text, model_id='fr-en')
    translation=translation_response.get_result()
    english_text =translation['translations'][0]['translation']
    return english_text
