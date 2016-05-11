"""
conway.images
~~~~~~~~~~~~~~~
This module contains the image creation logic.
"""

import os
import sys
from uuid import uuid4
from itertools import product

import png

import moviepy.editor as mpy
from imgurpython import ImgurClient

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')

ALBUM_HASH = os.environ.get('ALBUM_HASH')

SQUARE_SIZE = 4
BLACK = u' \u25A0'
WHITE = u' \u25A1'


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

def to_png(board, to_console=False):
    """
    Serializes the board as a png file.
    boolean: `to_console` if flag is True, it will print a string representation
    of the board to stdout, in addition to the file.
    """
    png_size = (board.size + 1)*SQUARE_SIZE
    writer = png.Writer(png_size, png_size, greyscale=True, bitdepth=1)

    lines = []
    line = []
    for i, j in product(range(board.size + 1), range(board.size + 1)):
        line.extend([0]*SQUARE_SIZE if (i, j) in board.points else [1]*SQUARE_SIZE)
        if to_console:
            sys.stdout.write(BLACK if (i, j) in board.points else WHITE)
        if j == board.size:
            for _ in range(SQUARE_SIZE):
                lines.append(line)
            if to_console:
                print()
            line = []

    board.frame_num += 1
    frame_name = str(board.frame_num) + '.png'
    with open(frame_name, 'wb') as frame:
        writer.write(frame, lines)


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
            # time.sleep(.05)
        to_png(board, to_console)
        seen.add(cur_board_repr)
        board = board.advance().constrain()

def upload_img(filename, description=None):
    client = ImgurClient(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN, REFRESH_TOKEN)
    image = client.upload_from_path(filename, config={'album': ALBUM_HASH,
                                                      'description': description or ''})
    return image['link']
