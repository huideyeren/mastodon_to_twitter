import settings
from mastodon import *
import tweepy


TWITTER_CONSUMER_KEY = settings.twi_con_key
TWITTER_CONSUMER_SECRET = settings.twi_con_seq
TWITTER_ACCESS_TOKEN = settings.twi_acc_tkn
TWITTER_ACCESS_SECRET = settings.twi_acc_seq

class Mas2twiAuth:
    def login_for_mastodon():
        mastodon = Mastodon(
            client_id="my_clientcred_nico.txt",
            access_token="my_usercred_nico.txt",
            api_base_url="https://friends.nico")
        return mastodon


    def login_for_twitter():
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        twitter = tweepy.API(auth)
        return twitter

tweet = "Pythonから試しにマストドンとTwitterに書き込んでみる。"

mstdn = Mas2twiAuth.login_for_mastodon()

twi = Mas2twiAuth.login_for_twitter()

twi.update_status(tweet)
mstdn.toot(tweet)



