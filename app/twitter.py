import logging
import time
import tweepy

from typing import TypedDict, Dict

from app.translation import Translation


class TwitterAccount(TypedDict):
    username: str
    language: str
    last_tweet_id: int


class Twitter():
    """"
    Class which interacts with Twitter API
    """

    def __init__(
        self,
        public_key: str,
        private_key: str,
        access_token: str,
        access_token_secret: str,
        deepl_auth_key: str,
        twitter_accounts: Dict[str, TwitterAccount],
    ):

        # API INITIALISATION
        self.api = self.create_api(
            key=public_key,
            private_key=private_key,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

        self.twitter_accounts = twitter_accounts

        self.keywords = [
            'video',
            'tiktok',
            'tik tok',
            'live',
            'youtube',
            'telegram',
            'instagram',
            'facebook',
            'sign up',
            'subscribe',
            'jeu concours',
            'jeux concours'
        ]

        self.translation = Translation(auth_key=deepl_auth_key)

    # INITIALIZE THE API'S CREATION
    def create_api(
        self,
        key: str,
        private_key: str,
        access_token: str,
        access_token_secret: str,
    ):
        logger = logging.getLogger()
        auth = tweepy.OAuthHandler(key, private_key)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(
            auth,
            wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True
        )
        try:
            api.verify_credentials()
        except Exception as e:
            logger.error("Error creating API", exc_info=True)
            raise e
        logger.info("API created")
        return api

    # POST TWEET
    def post_tweet(self, text: str):
        try:
            self.api.update_status(text)
            print('Tweet Posted')
        except tweepy.TweepError as error:
            if error.api_code == 187:
                print('Duplicate Message')
                time.sleep(5)

    # POST TEXT & MEDIA
    def upload_media(self, text: str, filename: str):
        media = self.api.media_upload(filename=filename)
        self.api.update_status(text, media_ids=[media.media_id_string])

    # RETWEET TWEETS CONTAINNING THE INPUT KEYWORDS
    def retweet(self, tweetID):
        try:
            self.api.retweet(tweetID)
            print('Tweet Retweeted')
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(5)

    # IGNORE IRELEVANT TWEETS
    def ignore_tweet(self, text: str) -> bool:
        i = 0
        while i < len(self.keywords):
            if self.keywords[i] in text.lower():
                print("Useless tweet")
                return True
            i += 1
        return False

    # AUTOMATICALLY POST OR RETWEET TWEETS
    def user_timeline(self, username: str):
        tweet = self.api.user_timeline(
            screen_name=username,
            # 200 is the maximum allowed count
            count=200,
            include_rts=False,
            # Necessary to keep full_text
            # otherwise only the first 140 words are extracted
            tweet_mode='extended'
        )[0]

        if tweet.id != self.twitter_accounts[username]['last_tweet_id'] \
                and not self.ignore_tweet(tweet.full_text):
            if self.twitter_accounts[username]['language'] == 'en':
                translated_news = self.translation.translate(tweet.full_text)
                print("ID: {}".format(tweet.id))
                print(tweet.full_text)
                self.post_tweet(translated_news + f'\n(source: {username})')
                # last_tweet = tweet
                self.twitter_accounts[username]['last_tweet_id'] = tweet.id
            elif self.twitter_accounts[username]['language'] == 'fr':
                print("ID: {}".format(tweet.id))
                print(tweet.full_text)
                self.retweet(tweet.id)
                # last_tweet = tweet
                self.twitter_accounts[username]['last_tweet_id'] = tweet.id

    # AUTOMATICALLY POST OR RETWEET TWEETS ACCORDING TO THE NEWS SOURCE
    def target_user_timeline(self):
        for username, _ in self.twitter_accounts.items():
            # Thread(target = self.user_timeline(username)).start()
            print(f'Getting account: {username}')
            self.user_timeline(username)
