#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tear_down_app():
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    states = storage.all(State)
    render_template("7-states_list.html", states=states)


app.run(host="0.0.0.0", port=5000)
