#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    states = storage.all(State).values()
    return render_template("10-hbnb_filters.html", states=states)


@app.teardown_appcontext
def teardown(err):
    """teardown app context"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0")
