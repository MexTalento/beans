# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import json

from yelp_beans.models import MeetingSubscription
from yelp_beans.models import UserSubscriptionPreferences
from yelp_beans.routes.api.v1.metrics import metrics_api


def test_get_metrics(app, minimal_database):

    with app.test_request_context('/v1/metrics'):
        response = metrics_api()
        assert '[]' == response

    MeetingSubscription(title='test1').put()

    with app.test_request_context('/v1/metrics'):
        response = metrics_api()
        assert json.dumps([{
            "meetings": 0,
            "subscribed": 0,
            "multiple_subscribed": 0,
            "week_participation": 0,
            "title": "test1",
            "usernames": []
        }]) == response


def test_get_metrics_multiple(app, database, subscription, fake_user):
    with app.test_request_context('/v1/metrics'):
        response = metrics_api()
        assert json.dumps([{
            "meetings": 0,
            "subscribed": 1,
            "multiple_subscribed": 0,
            "week_participation": 1,
            "usernames": ["darwin"],
            "title": "Yelp Weekly",
        }]) == response

    MeetingSubscription(title='test1').put()

    with app.test_request_context('/v1/metrics'):
        response = metrics_api()
        assert json.dumps([
            {
                "usernames": ["darwin"],
                "meetings": 0,
                "subscribed": 1,
                "multiple_subscribed": 0,
                "week_participation": 1,
                "title": "Yelp Weekly"
            },
            {
                "usernames": [],
                "meetings": 0,
                "subscribed": 0,
                "multiple_subscribed": 0,
                "week_participation": 0,
                "title": "test1"
            }
        ]) == response


def test_get_metrics_user_has_multiple_prefs_for_the_same_subscription(app, database, subscription, fake_user):
    preference = UserSubscriptionPreferences(
        preference=subscription.datetime[1],
        subscription=subscription.key,
    ).put()
    fake_user.subscription_preferences.append(preference)

    with app.test_request_context('/v1/metrics'):
        response = metrics_api()
        assert json.dumps([
            {
                "usernames": ["darwin"],
                "meetings": 0,
                "subscribed": 1,
                "multiple_subscribed": 1,
                "week_participation": 1,
                "title": "Yelp Weekly"
            }
        ]) == response
