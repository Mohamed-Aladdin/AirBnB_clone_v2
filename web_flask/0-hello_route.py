#!/usr/bin/python3
"""Flask app starter script"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Request fn to send hello"""

    return "Hello HBNB!"


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
