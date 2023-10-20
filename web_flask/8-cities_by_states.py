#!/usr/bin/python3

"""
Starts a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(_name_)


@app.route('/cities_by_states', strict_slashes=False)
def cities_route():
    """Comment"""
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if _name_ == '_main_':
    app.run(host='0.0.0.0')
