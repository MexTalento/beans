# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import json

from flask import Blueprint

from yelp_beans.logic.metrics import get_current_participation
from yelp_beans.logic.metrics import get_subscribed_users


metrics_blueprint = Blueprint('metrics', __name__)


@metrics_blueprint.route('/', methods=['GET'])
def metrics_api():
    metrics = get_subscribed_users()
    participation, participation_counts, meeting_request_counts = get_current_participation()

    for metric in metrics:
        subscription = metric['subscription_key']
        metric['week_participants'] = participation_counts.get(subscription, 0)
        metric['requested_meetings'] = meeting_request_counts.get(subscription, 0)
        metric['subscribed'] = len(metric['usernames'])
        metric['meetings'] = sum(len(count) for count in metric['requested_meetings'])
    return json.dumps(metrics)
