#!/usr/bin/python3
"""
This module starts a
Flask web application with the following specifications:
"""

from flask import Flask

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
