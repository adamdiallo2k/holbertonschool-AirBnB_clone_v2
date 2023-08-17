#!/usr/bin/python3
"""
This module starts a
Flask web application with the following specifications:
"""

from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Returns a string for the root route."""
    return "Hello HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """Returns a string with 'C' followed by the captured text."""
    text_with_spaces = text.replace("_", " ")
    return f'C {text_with_spaces}'


@app.route("/hbnb", strict_slashes=False)
def about():
    """Returns a string for the root route."""
    return "HBNB"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text):
    """Display 'Python', followed by the value of the text
    variable with underscores replaced by spaces."""
    text_with_spaces = text.replace("_", " ")
    return f'Python {text_with_spaces}'


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    if n.isdigit():
        return f'{n} is a number'
    else:
        return abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def numberTemp(n):
    """display “n is a number” only if n is an integer"""
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        return abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
