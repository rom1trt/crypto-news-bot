import tweepy
import logging

# CONSUMER KEYS
API_KEY = 'q2q8YZNxJXrWo0AryqEL0eXEJ'
API_PRIVATE_KEY = '559AWR7Lw4XNojsf9fG8xiCjJALoQEckF4xXHrUED5foDZUzZk'

# AUTHENTIFICATION TOKENS
ACCESS_TOKEN = '1380879035337744389-0yLbIVNHK6SHPXPMSWSvD0Zgroa405'
ACCESS_TOKEN_SECRET = 'EznGSY1tNjAKPKKMPpNFRyhXR3Hd0YVQUt2jMlu0W798s'

# INITIALIZE THE API'S CREATION
def create_api():
    logger = logging.getLogger()
    auth = tweepy.OAuthHandler(API_KEY, API_PRIVATE_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api