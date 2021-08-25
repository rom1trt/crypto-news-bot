# from app.config import DEEPL_AUTH_KEY
import requests
import json
import uuid
from googletrans import Translator

# TRANSLATE ANY ENGLISH NEWS TO FRENCH


class Translation:
    def __init__(self, auth_key: str):
        self.auth_key = auth_key

    def translate_deepl(self, text: str):
        """
        Translates from English to French (Deepl)
        Returns: translated text (str)
        """
        r = requests.post(
            url="https://api-free.deepl.com/v2/translate",
            data={"target_lang": "FR", "auth_key": self.auth_key, "text": f"{text}",},
        )
        my_json = json.loads(r.text)
        try:
            len(my_json["translations"]) > 0
            return my_json["translations"][0]["text"]
        except Exception:
            return "No text to translate or translation limit reached"

    def translate_microsoft(self, text: str):
        """
        Translates from English to French (Microsoft)
        Returns: translated text (str)
        """

        # Add your subscription key and endpoint
        subscription_key = "8d6ab89f3bf84a91919c2c8102aab6d1"
        endpoint = "https://api.cognitive.microsofttranslator.com/"

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = "westeurope"

        path = "/translate"
        constructed_url = endpoint + path

        params = {"api-version": "3.0", "from": "en", "to": ["fr"]}
        constructed_url = endpoint + path

        headers = {
            "Ocp-Apim-Subscription-Key": subscription_key,
            "Ocp-Apim-Subscription-Region": location,
            "Content-type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4()),
        }

        # You can pass more than one object in body.
        body = [{"text": text}]

        request = requests.post(
            constructed_url, params=params, headers=headers, json=body
        )
        response = request.json()
        return response[0]["translations"][0]["text"]

    def translate_news(self, news_list: list) -> list:
        """
        Translates from English to French
        Returns: List of translated news
        """
        translated_news = []
        for news in range(news_list):
            translated_news.append(self.translate_all(news))
        return translated_news

    def translate_all(self, text: str):
        """
        Translates text using both API and
        change when the words' limit is reached.
        Returns: translated news (str)
        """
        err = "No text to translate or translation limit reached"
        if self.translate_deepl(text) == err:
            print("used Microsoft")
            return self.translate_microsoft(text)
        else:
            print("used Deepl")
            return self.translate_deepl(text)
