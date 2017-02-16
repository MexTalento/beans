# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import json


class DataProvider(object):
    # TODO: docs

    # list of variables we need from the config
    config = []

    def load_config(self):
        with open("client_config.json") as config:
            full_config = json.loads(config.read())
            return {
                key: full_config[key]
                for key in self.config
            }

    def fetch(self):
        return None

    def munge(self, data):
        return data

    def __call__(self):
        return self.munge(self.fetch(*self.load_secrets()))
