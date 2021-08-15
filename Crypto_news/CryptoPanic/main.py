from api_gather import CryptoPanic
from Deepl.api_deepl import translate_news
import Twitter

# INITIALISATION OF BOTH NEWS' LANGUAGES WE NEED TO FETCH
test1 = CryptoPanic(kind = 'news', region = 'en')
test2 = CryptoPanic(kind = 'news', region = 'fr')

# FETCH THE LAST PIECE OF NEWS CONTINUOUSLY
def main():
    LOOP1 = True
    last_en_news = test1.get_last_news(3)
    last_french_news = test2.get_last_news(3)
    print(last_en_news)
    print(last_french_news)
    while LOOP1:
        boolean1 = False
        boolean2 = False
        while not boolean1 or not boolean2:
            new_last_en_news = test1.get_last_news(3)
            new_last_french_news = test2.get_last_news(3)
            if last_en_news != new_last_en_news:
                print(new_last_en_news)
                Twitter.post_tweet(new_last_en_news) #translate_news(new_last_en_news)
                last_en_news = new_last_en_news #translate_news(new_last_en_news)
                boolean1 = True
            if last_french_news != new_last_french_news:
                print(new_last_french_news)
                Twitter.post_tweet(new_last_french_news)
                last_french_news = new_last_french_news
                boolean2 = True  
        LOOP1 = False    
#main()
