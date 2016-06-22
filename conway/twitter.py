import os
import tweepy

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitter_client = tweepy.API(auth)
