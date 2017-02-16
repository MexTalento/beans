# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging


class DataProvider(object):
    # TODO: docs

    def load_secrets(self):
        logging.info("Loading secrets: {}".format(self.secrets))
        with open("client_config.json") as config:
            return {
                name: config[name]
                for name in json.loads(config.read())
            }

    def fetch(self):
        return None

    def munge(self, data):
        return data

    def __call__(self):
        return self.munge(self.fetch(*self.load_secrets()))
