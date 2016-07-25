"""
conway.server
~~~~~~~~~~~~~~~
This module contains the bot's logic.
"""
import os
import random

from collections import deque

from game import Board
from images import draw_frames, create_gif
from twitter import twitter_client

import redis
r = redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379"))

HASHTAGS = os.environ.get("HASHTAGS")
PROB = float(os.environ.get("PROB", "0.9"))

my_handle = "@" + twitter_client.me().screen_name

def grab_tweets():
    """
    Searches for the list of tweets since the last job execution.
    Yields relevant ones.
    """
    max_id = r.get('max_id')
    tweets = twitter_client.search(my_handle, since_id=max_id)
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
    pattern = create_pattern_from_text(original_tweet.text)
    gif_name = gif_from_pattern(pattern)
    user_name = original_tweet.user.screen_name
    message = "Hi @{}, look at the complexity of your tweet!\n{}".format(user_name, HASHTAGS)
    twitter_client.update_with_media(filename=gif_name, 
                                     status=message, 
                                     in_reply_to_status_id=original_tweet.id_str)

def generate_random_tweet():
    """
    Come up with a random pattern, tweet it.
    """
    with open('misc/emoji.txt') as f:
        lines = f.readlines()

    emoji = random.choice(lines)[:-1]
    options = (emoji, ' ', ' ')

    deck = deque()

    for _ in range(20):
        char = random.choice(options)
        deck.appendleft(char)
        deck.append(char)

    text = ''.join(deck).strip()
    text = text + '\n' + HASHTAGS

    pattern = create_pattern_from_text(text)
    gif_name = gif_from_pattern(pattern)
    twitter_client.update_with_media(filename=gif_name, 
                                     status=text)

def get_word_bin(string):
    """
    Given a string, returns its binary representation in 0s and 1s
    """
    return ''.join(format(ord(x), 'b') for x in string)

def create_pattern_from_text(text):
    """
    Given a tweet, returns a pattern of 0s, 1s and \n characters
    to be consumed to create a game of life board.
    """
    words = text.split(' ')
    return '\n'.join(get_word_bin(word) for word in words if word != my_handle)

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

    if random.random() > PROB:
        print("Random tweet! Let's see what we get...")
        generate_random_tweet()
    else:
        print("No random tweet this time!")

if __name__ == '__main__':
    main()
