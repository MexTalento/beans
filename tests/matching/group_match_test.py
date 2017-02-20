# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import logging

from yelp_beans.logic.subscription import get_specs_from_subscription
from yelp_beans.logic.subscription import store_specs_from_subscription
from yelp_beans.matching.group_match import generate_meetings
from yelp_beans.models import User
from yelp_beans.models import UserSubscriptionPreferences


def test_generate_meetings_with_history(minimal_database, subscription):
    preference = subscription.datetime[0]
    user_pref = UserSubscriptionPreferences(preference=preference, subscription=subscription.key).put()

    user1 = User(username='a', department='dept', subscription_preferences=[user_pref])
    user1.put()
    user2 = User(username='b', department='dept2', subscription_preferences=[user_pref])
    user2.put()
    user3 = User(username='c', department='dept', subscription_preferences=[user_pref])
    user3.put()
    user4 = User(username='d', department='dept2', subscription_preferences=[user_pref])
    user4.put()

    user_list = [user1, user2, user3, user4]
    week_start, specs = get_specs_from_subscription(subscription)
    store_specs_from_subscription(subscription.key, week_start, specs)

    result = {user.key for user in generate_meetings(user_list, specs[0], 3)}

    user_map = {}
    for user in user_list:
        user_map[user.key] = user

    all_users = set(user_map.keys())

    unmatched = all_users.difference(result)
    matches = result
    assert len(matches) == 3
    assert len(unmatched) == 1
    logging.info(unmatched)
    logging.info(matches)


'''
    meeting_history = set([
        (user1.key.id(), user2.key.id()),
        (user3.key.id(), user4.key.id()),
        (user2.key.id(), user3.key.id()),
        (user1.key.id(), user4.key.id()),
    ])
    matches, unmatched = generate_meetings(user_list, specs[0], 3, meeting_history)
    assert len(matches) == 0
    assert len(unmatched) == 4

    meeting_history = set([
        (user1.key.id(), user2.key.id()),
        (user3.key.id(), user4.key.id()),
        (user2.key.id(), user3.key.id()),
    ])
    matches, unmatched = generate_meetings(user_list, specs[0], 3, meeting_history)
    assert len(matches) == 1
    assert len(unmatched) == 2
'''
