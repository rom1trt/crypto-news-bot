import requests
import json
from googletrans import Translator

# TRANSLATE ANY ENGLISH NEWS TO FRENCH


class Translation():
    def __init__(self, auth_key: str):
        self.auth_key = auth_key

    def translate_deepl(self, text: str):
        """
        Translates from English to French (Deepl)
        Returns: translated text (str)
        """
        r = requests.post(
                        url='https://api-free.deepl.com/v2/translate',
                        data={
                            'target_lang': 'FR',
                            'auth_key': self.auth_key,
                            'text': f'{text}',
                        }
                    )
        my_json = json.loads(r.text)
        if len(my_json['translations']) > 0:
            return my_json['translations'][0]['text']
        else:
            return 'No text to translate or translation limit reached'

    def translate_google(self, text):
        """
        Translates from English to French (Google)
        Returns: translated text (str)
        """
        translator = Translator()
        translated = translator.translate(text, dest='fr')
        print(translated.text)
        return translated.text

    def translate_news(self, news_list: list) -> list:
        """
        Translates from English to French
        Returns: List of translated news
        """
        translated_news = []
        for news in range(news_list):
            translated_news.append(self.translate(news))
        return translated_news

    def translate_all(self, text):
        """
        Translates text using both API and
        change when the words' limit is reached.
        Returns: translated news (str)
        """
        err = 'No text to translate or translation limit reached'
        test_deepl = self.translate_deepl(text)
        if test_deepl == err:
            print('Used Google Translate')
            return self.translate_google(text)
        else:
            print('Used Deepl')
            return test_deepl
