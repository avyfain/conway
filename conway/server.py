"""
conway.server
~~~~~~~~~~~~~~~
This module contains the web server logic.
"""

from game import Board
from images import draw_frames, create_gif, upload_img
from examples import SOME

from flask import Flask, request, render_template, make_response
from functools import wraps, update_wrapper
from datetime import datetime


app = Flask(__name__)
app.debug = True

@app.route('/')
def form():
    """
    Renders the form file html.
    """
    return render_template("form.html")

@app.route('/', methods=['POST'])
def form_post():
    print(request.form)
    pat = request.form['input_pattern']
    processed_pat = imgur_from_pattern(pat)
    return render_template("form.html", gif=processed_pat)

def imgur_from_pattern(pattern=SOME):
    """
    Main application logic: given a conway pattern
    from the lexicon, it returns a link to the image on imgur
    """
    draw_frames(Board(pattern))
    name = create_gif()
    link = upload_img(name)
    return(link)

if __name__ == '__main__':
    app.run()
