#!/usr/bin/env python3

import flask

APP = flask.Flask(__name__)

@APP.route('/')
def index():
    return flask.render_templates('index.html')

if __name__ == '__main__':
    APP.debug=True
    APP.run()
