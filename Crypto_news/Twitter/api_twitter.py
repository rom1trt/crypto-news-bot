#from Deepl.api_deepl import translate_news
#from Deepl.api_deepl import translate_news
import tweepy
from config import *
from threading import Thread
import time

# API INITIALISATION
api = create_api()

dic = {
    'CoinDesk': 'en',
    'CoinTelegraph': 'en',
    'LeJournalDuCoin': 'fr',
    'cryptoastblog': 'fr'
}

# POST TWEET
def post_tweet(text: str):
    try:
        api.update_status(text)
    except tweepy.TweepError as error:
        if error.api_code == 187:
            # Do something special
            print('duplicate message')
            time.sleep(10)

# POST TEXT & MEDIA
def upload_media(text: str, filename: str):
    media = api.media_upload(filename = filename)
    api.update_status(text, media_ids = [media.media_id_string])

# RETWEET TWEETS CONTAINNING THE INPUT KEYWORDS
def retweet(keywords):
    number_of_tweets = 3
    for tweet in tweepy.Cursor(api.search, keywords, lang = 'fr').items(number_of_tweets):
        try:
            tweet.retweet()
            print('Tweet Retweeted')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# AUTOMATICALLY RETWEET TWEETS
def user_timeline(userID: str):
    last_tweet = ""
    tweet = api.user_timeline(screen_name = userID, 
                        # 200 is the maximum allowed count
                        count = 200,
                        include_rts = False,
                        # Necessary to keep full_text 
                        # otherwise only the first 140 words are extracted
                        tweet_mode = 'extended'
                        )[1]
    
    if tweet != last_tweet:
        if dic[userID] == 'en':
            #translated_news = translate_news(tweet.full_text)
            print("ID: {}".format(tweet.id))
            print(tweet.created_at)
            print('TRADUCTION!!')
            print(tweet.full_text)
            post_tweet(tweet.full_text) #translated_news)
            print("\n")
            last_tweet = tweet
        elif dic[userID] == 'fr':
            print("ID: {}".format(tweet.id))
            print(tweet.created_at)
            print('PAS DE TRADUCTION!!')
            print(tweet.full_text)
            retweet(tweet.id)
            print("\n")
            last_tweet = tweet

def target_user_timeline(usernames):
    while True:
        # thread1 = Thread(target = user_timeline(usernames[0]))
        # thread1.start()
        # time.sleep(5)

        # thread2 = Thread(target = user_timeline(usernames[1]))
        # thread2.start() 
        # time.sleep(5)
        for username in usernames:
            Thread(target = user_timeline(username)).start() 
            time.sleep(10)   
target_user_timeline(['cryptoastblog', 'LeJournalDuCoin'])
