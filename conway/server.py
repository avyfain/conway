"""
conway.server
~~~~~~~~~~~~~~~
This module contains the web server logic.
"""
from flask import Flask, request, make_response

from conway.game import Board
from conway.images import draw_frames, create_gif, upload_img
from conway.examples import SOME
from conway.utils import crossdomain


app = Flask(__name__)
app.debug = True

@app.route('/test', methods=['GET', 'POST', 'OPTIONS'])
@crossdomain(origin='*')
def form_post():
    print(request.form)
    pat = request.form['input_pattern']
    processed_pat = imgur_from_pattern(pat)
    return processed_pat

def imgur_from_pattern(pattern=SOME):
    """
    Main application logic: given a conway pattern
    from the lexicon, it returns a link to the image on imgur
    """
    draw_frames(Board(pattern))
    name = create_gif()
    # link = upload_img(name, description=pattern)
    return(name)

if __name__ == '__main__':
    app.run()
