"""
conway.server
~~~~~~~~~~~~~~~
This module contains the web server logic.
"""
import os

from game import Board
from images import draw_frames, create_gif
from twitter import twitter_client

import redis
r = redis.from_url(os.environ.get("REDIS_URL"))

def grab_tweets():
    tweet = None
    max_id = r.get('max_id')
    while not tweet:
        tweets = twitter_client.search('@tweetgameoflife', max_id)
        try:
            tweet = next(tweet for tweet in tweets if '://' not in tweet.text and \
                                                      not tweet.text.startswith('RT'))
            r.set('max_id', tweets[0].id_str)
            return tweet
        except StopIteration:
            return None

def reply_with_conway():
    original_tweet = grab_tweets()
    if original_tweet:
        pattern = create_pattern_from_tweet(original_tweet)
        gif_name = gif_from_pattern(pattern)
        user_name = original_tweet.user.screen_name
        message = "Hi @{}, look at the complexity of your tweet!".format(user_name)
        twitter_client.update_with_media(filename=gif_name, 
                                  status=message, 
                                  in_reply_to_status_id=original_tweet.id_str)
    else:
        print("No one is tweeting, try again later :(")

def get_word_bin(string):
    return ''.join(format(ord(x), 'b') for x in string)

def create_pattern_from_tweet(original_tweet):
    words = original_tweet.text.split(' ')
    return '\n'.join([get_word_bin(word) for word in words])

def gif_from_pattern(pattern):
    """
    Main application logic: given a conway pattern
    from the lexicon, it returns a link to the image on imgur
    """
    draw_frames(Board(pattern))
    name = create_gif()
    return name

if __name__ == '__main__':
    reply_with_conway()
