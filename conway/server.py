"""
conway.server
~~~~~~~~~~~~~~~
This module contains the web server logic.
"""

from conway.game import Board
from conway.images import draw_frames, create_gif
from conway.tweet import twitter

def grab_random_tweet():
    tweet = None
    max_id = None
    while not tweet:
        tweets = twitter.search('algorithm', max_id=max_id)
        tweet = next(tweet for tweet in tweets if '://' not in tweet.text and \
                                                  'RT'  not in tweet.text)
        print(tweet.text)
        max_id = tweets[-1].id
    return tweet

def reply_with_conway():
    original_tweet = grab_random_tweet()
    print(original_tweet)
    pattern = create_pattern_from_tweet(original_tweet)
    gif_name = gif_from_pattern(pattern)
    user_name = original_tweet.user.screen_name
    message = "Hi {}, look at the complexity of your tweet!".format(user_name)
    twitter.update_with_media(gif_name, message)

def get_word_bin(string):
    return ''.join(format(ord(x), 'b') for x in string)

def pattern_from_string(string):
    words = string.split(' ')
    return '\n'.join([get_word_bin(word) for word in words])

def create_pattern_from_tweet(original_tweet):
    pat = pattern_from_string(original_tweet.text)
    return processed_pat

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
