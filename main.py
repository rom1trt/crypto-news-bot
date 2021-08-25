import time
from typing import Dict

from app.config import (
    CRYPTOPANIC_API_KEY,
    DEEPL_AUTH_KEY,
    TWITTER_API_KEY,
    TWITTER_API_PRIVATE_KEY,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET,
)
from app.cryptopanic import CryptoPanic
from app.twitter import Twitter, TwitterAccount
from app.translation import Translation

translation_text = Translation(DEEPL_AUTH_KEY)

twitter_accounts: Dict[str, TwitterAccount] = {
    "CoinTelegraph": TwitterAccount(
        username="CoinTelegraph", language="en", last_tweet_id=0,
    ),
    "CoinDesk": TwitterAccount(username="CoinDesk", language="en", last_tweet_id=0,),
    "whale_alert": TwitterAccount(
        username="whale_alert", language="en", last_tweet_id=0,
    ),
    "CryptanalystFR": TwitterAccount(
        username="CryptanalystFR", language="fr", last_tweet_id=0,
    ),
    "coinalist": TwitterAccount(username="coinalist", language="fr", last_tweet_id=0,),
    "BTCTN": TwitterAccount(username="BTCTN", language="en", last_tweet_id=0,),
    "cryptoastblog": TwitterAccount(
        username="cryptoastblog", language="fr", last_tweet_id=0,
    ),
    "LeJournalDuCoin": TwitterAccount(
        username="LeJournalDuCoin", language="fr", last_tweet_id=0,
    ),
}

twitter = Twitter(
    public_key=TWITTER_API_KEY,
    private_key=TWITTER_API_PRIVATE_KEY,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
    deepl_auth_key=DEEPL_AUTH_KEY,
    twitter_accounts=twitter_accounts,
)

cryptopanic_fr = CryptoPanic(
    api_key=CRYPTOPANIC_API_KEY, region="fr", deepl_auth_key=DEEPL_AUTH_KEY
)

cryptopanic_en = CryptoPanic(
    api_key=CRYPTOPANIC_API_KEY, region="en", deepl_auth_key=DEEPL_AUTH_KEY
)

LOOP1 = True
while LOOP1:
    # Twitter Accounts
    twitter.target_user_timeline()
    time.sleep(5)

    # CryptoPanic
    # last_en_news = cryptopanic_en.get_last_news()
    # last_french_news = cryptopanic_fr.get_last_news()
    # boolean1, boolean2 = False, False
    # while not boolean1 or not boolean2:
    #     new_last_en_news = cryptopanic_en.get_last_news()
    #     new_last_french_news = cryptopanic_fr.get_last_news()
    #     if last_en_news != new_last_en_news:
    #         en_source = cryptopanic_en.get_last_source()
    #         print(new_last_en_news)
    #         translated_news = translation_text.translate_all(new_last_en_news)
    #         twitter.post_tweet(translated_news + "\n" + en_source)
    #         last_en_news = new_last_en_news
    #         boolean1 = True
    #     if last_french_news != new_last_french_news:
    #         fr_source = cryptopanic_fr.get_last_source()
    #         print(new_last_french_news + "\n" + fr_source)
    #         twitter.post_tweet(new_last_french_news + " " + fr_source)
    #         last_french_news = new_last_french_news
    #         boolean2 = True
    # LOOP1 = False
