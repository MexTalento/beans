# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import logging

import requests
from requests.auth import HTTPBasicAuth

from yelp_beans.data_providers.amazon_s3 import get_json_employee_data_from_s3
from yelp_beans.data_providers.data_provider import DataProvider


class RestProvider(DataProvider):

    config = [
        'rest_user',
        'rest_password',
        'rest_url'
    ]

    def fetch(self, user, password):
        return requests.get(
            self.url,
            auth=HTTPBasicAuth(user, password),
            timeout=60.0,
        ).json()


def get_json_employee_data():
    logging.info('Reading employees file from S3...')
    employee_data = RestProvider()

    # TODO remove once we find a solution for photos
    s3_data = get_json_employee_data_from_s3()

    new_employee_data = []
    for data in employee_data:
        user = {
            'email': data['work_email'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            # TODO fix once we find a solution for photos
            'photo_url': s3_data[data['work_email']]['photo_url'],
        }

        required = {'email', 'first_name', 'last_name', 'photo_url'}
        not_required = set(data.keys()) - required

        user['metadata'] = {attr: data[attr] for attr in not_required}
        user['metadata'] = {
            'company_profile_url': s3_data[user['email']]['company_profile_url'],
            'username': data['work_email'].split('@')[0]
        }
        new_employee_data.append(user)

    return new_employee_data
