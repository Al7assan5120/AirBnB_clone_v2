#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """/c/<text>"""
    text_new = text.replace('_', ' ')
    return f'C {escape(text_new)}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def py_text(text='is cool'):
    """/python/<text>"""
    text_new = text.replace('_', ' ')
    return f'Python {escape(text_new)}'


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """/number/<n>"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def int_num(n):
    """/number_template/<n>"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def mod2_num(n):
    """/number_odd_or_even/<n>"""
    if n % 2 == 0:
        text = 'even'
    else:
        text = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
