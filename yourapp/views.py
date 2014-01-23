"""
    deploy.app.views
    ~~~~~~~~~~~~~~~~

    Register your actions.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
from yourapp import app


@app.route('/')
def index():
    return 'Hello!'
