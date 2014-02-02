"""
    deploy.app
    ~~~~~~~~~~

    One simple WSGI app.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
from flask import Flask
app = Flask(__name__)
from yourapp import settings
app.config.from_object(settings)

import yourapp.views
