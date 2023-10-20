#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """list all states"""
    states = storage.all(State)
    render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_downapp(error):
    """clean up all the states"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
