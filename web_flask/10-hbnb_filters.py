#!/usr/bin/python3

"""
Starts a Flask web application
"""

from models import storage
from models.amenity import Amenity
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(_name_)


@app.route('/hbnb_filters', strict_slashes=False)
def filters_list():
    """Comment"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template(
        "10-hbnb_filters.html",
        states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if _name_ == '_main_':
    app.run(host='0.0.0.0')
