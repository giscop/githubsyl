#!/usr/bin/env python3

import flask


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ 显示可在 '/' 访问的 index 页面
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    APP.debug=True
    APP.run()