"""
CryptoPanic API Wrapper.
Docs for API found here. https://cryptopanic.com/developers/api/
CryptoPanic Server is cached every 30 seconds. So crawling at a faster rate is pointless.
All API methods are rate limited per IP at 5req/sec.
"""
#from Deepl.api_deepl import translate_news
import Deepl
import requests
import json
import pandas as pd
from CryptoPanic.config_example import API_KEY
import time
import Twitter

global_api_rate_delay = 0.2  # All API methods are rate limited per IP at 5req/sec.

class CryptoPanic():

    url = f'https://cryptopanic.com/api/v1/posts/?auth_token={API_KEY}&public=true'

    def __init__(self, url = url, currencies = None, kind = None, region = None, page = None, number = 3):
        """
        Handles URL variables for API POST
        """
        self.number = number 

        if currencies is not None:
            if len(currencies.split(',')) <= 50:
                self.currencies = currencies
                url += "&currencies={}".format(currencies)
            else:
                print("Warning: Maximum self.number of currencies is 50")

        kinds = ['news', 'media']
        if kind is not None and kind in kinds:
            self.kind = kind
            url += "&kind={}".format(kind)
        elif kind is not None and kind not in kinds:
            print('Warning: Kind is not available')

        regions = ['en', 'de', 'es', 'fr', 'it', 'pt', 'ru']  # (English), (Deutsch), (Español), (Français), (Italiano), (Português), (Русский)--> Respectively
        if region is not None and region in regions:
            self.region = region
            url += "&region={}".format(region)
        elif region is not None and region not in regions:
            print('Warning: Region is not available')

        if page is not None:
            url += f"&page={page}"
        if region == 'fr':
            self.url = 'https://cryptopanic.com/api/v1/posts/?auth_token=f3322769569c9c952301819406f554c1c818cf6d&public=true&kind=news&regions=fr'
        else:
            self.url = url

    def get_whole_page(self):
        page = requests.get(self.url)
        my_json = json.loads(page.text)
        return my_json

    def get_news_titles(self):
        """
        Get news titles
        Returns: List of news titles
        """
        time.sleep(global_api_rate_delay)
        news_titles = []
        my_json_page = self.get_whole_page()

        for i in range(self.number):
            news_titles.append(my_json_page["results"][i])

        return news_titles

    def get_source(self):
        """
        Gets news sources
        Returns: List of news' sources
        """
        time.sleep(global_api_rate_delay)
        news_sources = []
        my_json_page = self.get_whole_page()

        for i in range(self.number):
            news_sources.append(my_json_page["results"][i]["domain"])

        return news_sources

    def aggregate_data(self):
        """
        Gathers sources and news titles 
        Returns: Dictionary
        """
        if self.region == 'en':
            translated_news = self.get_news_titles(self.number) #translate_news(self.get_news_titles(self.self.number))
        else:
            translated_news = self.get_news_titles(self.number)
        sources = self.get_source(self.number)
        dict = {}
        j = 0
        for i in range(len(translated_news)):
            dict[translated_news[i]] = sources[j]
            j += 1
        return dict

    def get_df(self):
        """
        Returns: pandas DF
        """
        news = self.get_news_titles(self.self.number) 
        translated_news = Deepl.translate_news(self.get_news_titles(self.self.number))
        sources = self.get_source(self.self.number)
        df = pd.DataFrame(news, columns =['News'])
        df['Translated News'] = translated_news
        df['Sources'] = sources

        return df
    
    def get_last_news(self):
        return self.get_news_titles()[0]

test1 = CryptoPanic(kind = 'news', region = 'en')
test2 = CryptoPanic(kind = 'news', region = 'fr')

def main():
    LOOP1 = True
    last_en_news = test1.get_last_news()
    last_french_news = test2.get_last_news()
    print(last_en_news)
    print(last_french_news)
    while LOOP1:
        boolean1 = False
        boolean2 = False
        while not boolean1 or not boolean2:
            new_last_en_news = test1.get_last_news()
            new_last_french_news = test2.get_last_news()
            if last_en_news != new_last_en_news:
                en_source = test1.get_source()[0]
                print(new_last_en_news)
                Twitter.post_tweet(new_last_en_news + " " + en_source) #translate_news(new_last_en_news)
                last_en_news = new_last_en_news #translate_news(new_last_en_news)
                boolean1 = True
            if last_french_news != new_last_french_news:
                fr_source = test1.get_source()[0]
                print(new_last_french_news + " " + fr_source)
                Twitter.post_tweet(new_last_french_news + " " + fr_source)
                last_french_news = new_last_french_news
                boolean2 = True  
        LOOP1 = False    
#main()
