from mastodon import *
from tweepy import *
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class TootConfig(object):
    """Configure Mastodon and Twitter."""

    def login_for_mastodon(self):
        mastodon = Mastodon(
            client_id="my_clientcred_nico.txt",
            access_token="my_usercred_nico.txt",
            api_base_url="https://friends.nico")
        return mastodon

    def login_for_twitter(self):
        auth = tweepy.OAuthHandler(
            TWITTER_CONSUMER_KEY,
            TWITTER_CONSUMER_SECRET)
        auth.set_access_token(
            TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        twitter = tweepy.API(auth)
        return twitter

tweet = TootConfig().login_for_twitter()

public_tweets = tweet.home_timeline()
for tweet in public_tweets:
    print tweet.text
