"""
conway.images
~~~~~~~~~~~~~~~
This module contains the image creation logic.
"""

import os
import sys
import time

import moviepy.editor as mpy

from uuid import uuid4
from imgurpython import ImgurClient

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')

def create_gif():
    file_names = (fn for fn in os.listdir('.') if fn.endswith('.png'))
    s_file_names = sorted(file_names, key=lambda x: int(x.split('.')[0]))
    clip = mpy.ImageSequenceClip(s_file_names, fps=12)
    name = 'img/' + str(uuid4()) + '.gif'
    clip.write_gif(name, fps=12)
    delete_pngs()
    return name

def delete_pngs():
    for img in os.listdir('.'):
        if img.endswith('.png'):
            os.remove(img)

def draw_frames(board, max_steps=150, to_console=False):
    board.center()
    seen = set()

    delete_pngs()

    for i in range(max_steps):
        cur_board_repr = hash(board)
        if cur_board_repr in seen:
            break
        if to_console:
            sys.stdout.write('\033[H')  # move to the top
            sys.stdout.write('\033[J')  # clear the screen
            print('step:', i+1, '/', max_steps)
        board.to_png(to_console)
        time.sleep(.05)
        seen.add(cur_board_repr)
        board = board.advance().constrain()

def upload_img(filename):
    client = ImgurClient(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN, REFRESH_TOKEN)
    image = client.upload_from_path(filename)
    return image['link']
