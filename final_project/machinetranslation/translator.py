"""System module."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url )

def english_to_french(english_text):

    """
    This code acts as a translator from English to French
    """
    # Translate
    model_id = 'en-fr'
    french_text = language_translator.translate(
    text=english_text.lower(),
    model_id=model_id).get_result()
    # Print results
    return french_text.get("translations")[0].get("translation")


def french_to_english(french_text):
    """
    This code acts as a translator from French to English
    """
    # Translate
    model_id = 'fr-en'
    english_text = language_translator.translate(
    text=french_text,
    model_id=model_id).get_result()
    # Print results
    return english_text.get("translations")[0].get("translation")







print(english_to_french('green'))
print("\n")
print(french_to_english('bonjour'))