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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
