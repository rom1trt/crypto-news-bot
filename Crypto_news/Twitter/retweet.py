import tweepy
import logging
from config import create_api
from api_twitter import *
from multiprocessing import Process
import time
#from Deepl import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info = True)

    def on_error(self, status):
        logger.error(status)

def stream(accounts, tweets_listener):
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(follow = accounts, languages = ["fr"], is_async = True)

api = create_api() 
tweets_listener = FavRetweetListener(api)
accounts = ['482477197', '862443172089253893', '2207129125']

def run_cpu_tasks_in_parallel(tasks):
    running_tasks = [Process(target = task) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()

#run_cpu_tasks_in_parallel([stream(accounts, tweets_listener), user_timeline('CoinTelegraph')])
#stream(accounts, tweets_listener)
#user_timeline('CoinTelegraph')
#run_cpu_tasks_in_parallel([stream(accounts, tweets_listener), user_timeline('CoinTelegraph')])
target_user_timeline(['CoinDesk', 'CoinTelegraph', 'cryptoastblog', 'LeJournalDuCoin'])
