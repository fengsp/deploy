"""
    deploy.app
    ~~~~~~~~~~

    One simple WSGI app.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
from flask import Flask
app = Flask(__name__)
import yourapp.views


app.config.from_object('yourapp.settings')
