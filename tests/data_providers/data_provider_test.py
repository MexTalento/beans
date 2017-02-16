# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import json

import pytest


def test_get_secret_file(tmpdir):
    with tmpdir.as_cwd():
        expected = 'password'
        with open(tmpdir.join('client_config.json').strpath, 'w') as secrets:
            secret = {'secret': expected}
            secrets.write(json.dumps(secret))


def test_get_secret_file_no_exist(tmpdir):
    with tmpdir.as_cwd():
        with pytest.raises(IOError):
            pass
