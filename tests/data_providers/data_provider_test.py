# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import json

import pytest

from yelp_beans.data_providers.rest_endpoint import RestProvider


def test_rest_provider():
    provider = RestProvider()
    assert provider


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
