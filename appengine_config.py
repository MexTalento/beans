# -*- coding: utf-8 -*-
"""
`appengine_config.py` is automatically loaded when Google App Engine
starts a new instance of your application. This runs before any
WSGI applications specified in app.yaml are loaded.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from google.appengine.ext import vendor

# Third-party libraries are stored in "site-packages" in the virtualenv,
# vendoring will makes sure that they are importable by the application.
vendor.add('venv/lib/python2.7/site-packages/')
