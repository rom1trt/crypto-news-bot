import requests
import json

# TRANSLATE ANY ENGLISH NEWS TO FRENCH
def translate_news(news_list):
    """
    Translates from English to French
    Returns: List of translated news
    """
    translated_news = []
    for i in range(len(news_list)):
        r = requests.post(
            url = "https://api-free.deepl.com/v2/translate", 
            data = {"target_lang": "FR", "auth_key": '94011d83-33c5-8b9d-5a07-581d6a926eb7:fx', "text": "{0}".format(news_list[i])}
            )
        my_json = json.loads(r.text)
        translated_news.append(my_json["translations"][0]["text"])
    return translated_news
