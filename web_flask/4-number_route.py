#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    """display some text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    """display some text"""
    return "HBNB"


@app.route('/c/<text>')
def git_text(text):
    """display some text"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python(text):
    """display some text"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>')
def number(n):
    """display some text"""
    return f"{escape(n)} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
