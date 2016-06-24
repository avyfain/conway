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
    """
    Searches for the list of tweets since the last job execution.
    Yields relevant ones.
    """
    max_id = r.get('max_id')
    tweets = twitter_client.search('@tweetgameoflife', since_id=max_id)
    if tweets:
        r.set('max_id', str(tweets[0].id))
    else:
        print("No one is tweeting, try again later :(")
    
    for tweet in reversed(tweets):
        if '://' not in tweet.text and not tweet.text.startswith('RT'):
            yield tweet


def reply_with_conway(original_tweet):
    """
    Given a tweet, builds a gif and replies to the user.
    """
    pattern = create_pattern_from_tweet(original_tweet)
    gif_name = gif_from_pattern(pattern)
    user_name = original_tweet.user.screen_name
    message = "Hi @{}, look at the complexity of your tweet!".format(user_name)
    twitter_client.update_with_media(filename=gif_name, 
                              status=message, 
                              in_reply_to_status_id=original_tweet.id_str)

def get_word_bin(string):
    """
    Given a string, returns its binary representation in 0s and 1s
    """
    return ''.join(format(ord(x), 'b') for x in string)

def create_pattern_from_tweet(original_tweet):
    """
    Given a tweet, returns a pattern of 0s, 1s and \n characters
    to be consumed to create a game of life board.
    """
    words = original_tweet.text.split(' ')
    return '\n'.join([get_word_bin(word) for word in words])

def gif_from_pattern(pattern):
    """
    Given a conway pattern string, builds a board, draws its frames and writes the .gif file
    Returns name of new file.
    """
    draw_frames(Board(pattern))
    name = create_gif()
    return name

def main():
    """
    Main application logic
    """
    tweets = grab_tweets()
    for tweet in tweets:
        reply_with_conway(tweet)


if __name__ == '__main__':
    main()
