import json
import requests
import time

import pandas as pd

from typing import Dict
from app.translation import Translation


# All API methods are rate limited per IP at 5req/sec.
GLOBAL_API_RATE_DELAY = 0.2


class CryptoPanic():
    """
    Class which interacts with the CryptoPanic API
    """

    def __init__(
        self,
        api_key: str,
        deepl_auth_key: str,
        region: str = 'fr',
        number: int = 2,
    ):
        """
        Handles URL variables for API POST
        """
        self.translation = Translation(auth_key=deepl_auth_key)
        self.number = number
        self.region = region
        self.base_url = 'https://cryptopanic.com/api/v1/posts/?auth_token=' \
            + f'{api_key}&public=true&kind=news'
        self.url = self.base_url + f'&regions={self.region}'

        supported_region = ['en', 'fr']
        if region in supported_region:
            self.url = self.base_url + f'&regions={region}'
        else:
            print(f'Warning: Region {self.region} is not available')

    def get_whole_page(self):
        page = requests.get(self.url)
        my_json = json.loads(page.text)
        return my_json

    def get_news_titles(self) -> list:
        """
        Get news titles
        Returns: List of news titles
        """
        time.sleep(GLOBAL_API_RATE_DELAY)
        news_titles = []
        my_json_page = self.get_whole_page()

        if self.region == 'en':
            for i in range(self.number):
                news_titles.append(
                    self.translation.translate_all(
                        my_json_page["results"][i]['title']
                    )
                )
        elif self.region == 'fr':
            for i in range(self.number):
                news_titles.append(my_json_page["results"][i]['title'])

        return news_titles

    def get_source(self) -> list:
        """
        Gets news sources
        Returns: List of news' sources
        """
        time.sleep(GLOBAL_API_RATE_DELAY)
        news_sources = []
        my_json_page = self.get_whole_page()

        for i in range(self.number):
            news_sources.append(my_json_page["results"][i]["domain"])

        return news_sources

    def aggregate_data(self) -> Dict[str, str]:
        """
        Gathers sources and news titles
        Returns: Dictionary
        """
        if self.region == 'en':
            translated_news = self.get_news_titles(self.number)
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
        sources = self.get_source(self.self.number)
        df = pd.DataFrame(news, columns=['News'])
        # df['Translated News'] = translated_news
        df['Sources'] = sources

        return df

    def get_last_news(self) -> str:
        return self.get_news_titles()[0]

    def get_last_source(self) -> str:
        return self.get_source()[0]
