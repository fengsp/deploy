# -*- coding: utf-8 -*-
"""
    deploy.app.settings
    ~~~~~~~~~~~~~~~~~~~

    App config.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""

import os


DEBUG = False
if os.path.exists(os.path.join(os.path.dirname(__file__), 'debug')):
    DEBUG = True

