#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """display some text"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """display some text"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def git_text(text):
    """display some text"""
    return f"{escape(text)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
