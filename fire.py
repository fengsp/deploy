# -*- coding: utf-8 -*-
"""
    deploy.fire
    ~~~~~~~~~~~

    Fire your app up.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from yourapp import app


if __name__ == "__main__":
    app.run()
