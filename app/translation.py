import requests
import json

# TRANSLATE ANY ENGLISH NEWS TO FRENCH


class Translation():
    def __init__(self, auth_key: str):
        self.auth_key = auth_key

    def translate(self, text: str):
        r = requests.post(
                        url='https://api-free.deepl.com/v2/translate',
                        data={
                            'target_lang': 'FR',
                            'auth_key': 'fc6b0902-4c2f-4eb4-bbfe-739d36a79459',
                            'text': f'{text}',
                        }
                    )
        my_json = json.loads(r.text)
        if len(my_json['translations']) > 0:
            return my_json['translations'][0]['text']
        else:
            return 'No text to translate or translation limit reached'

    def translate_news(self, news_list: list) -> list:
        """
        Translates from English to French
        Returns: List of translated news
        """
        translated_news = []
        for news in range(news_list):
            translated_news.append(self.translate(news))
        return translated_news
