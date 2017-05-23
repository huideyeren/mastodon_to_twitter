import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

twi_con_key = os.environ.get("TWITTER_CONSUMER_KEY")
twi_con_seq = os.environ.get("TWITTER_CONSUMER_SECRET")
twi_acc_tkn = os.environ.get("TWITTER_ACCESS_TOKEN")
twi_acc_seq = os.environ.get("TWITTER_ACCESS_SECRET")