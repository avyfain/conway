"""
conway.images
~~~~~~~~~~~~~~~
This module contains the image creation logic.
"""

import os
from uuid import uuid4

import png

import moviepy.editor as mpy

DEFAULT_SQUARE_SIZE = 4
BLACK = u' \u25A0'
WHITE = u' \u25A1'

def create_gif():
    file_names = (fn for fn in os.listdir('.') if fn.endswith('.png'))
    s_file_names = sorted(file_names, key=lambda x: int(x.split('.')[0]))
    clip = mpy.ImageSequenceClip(s_file_names, fps=12)
    name = '{}.gif'.format(uuid4())
    clip.write_gif(name, fps=12)
    delete_pngs()
    return name

def delete_pngs():
    for img in os.listdir('.'):
        if img.endswith('.png'):
            os.remove(img)

def to_png(board, square_size=DEFAULT_SQUARE_SIZE):
    """
    Serializes the board as a png file.
    """
    png_size = (board.size + 1)*square_size
    writer = png.Writer(png_size, png_size, greyscale=True, bitdepth=1)

    lines = board.scale(square_size)
    board.frame_num += 1
    frame_name = '{}.png'.format(board.frame_num)
    with open(frame_name, 'wb') as frame:
        writer.write(frame, lines)

def draw_frames(board, max_steps=150):
    board.center()
    seen = set()

    delete_pngs()

    for _ in range(max_steps):
        cur_board_repr = hash(board)
        if cur_board_repr in seen:
            break
        to_png(board)
        seen.add(cur_board_repr)
        board = board.advance().constrain()
