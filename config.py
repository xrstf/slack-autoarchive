"""
All settings you can change for running slack channel reaper will live in this file.
"""

import os
from datetime import datetime, timedelta


def get_channel_reaper_settings():
    """ This returns a dictionary of all settings. """
    days_inactive = int(os.environ.get('DAYS_INACTIVE', 60))
    return {
        'admin_channel': os.environ.get('ADMIN_CHANNEL', ''),
        'days_inactive': days_inactive,
        # set MIN_MEMBERS and any channels with more members than
        # MIN_MEMBERS are exempt from archiving. 0 is no limit.
        'min_members': int(os.environ.get('MIN_MEMBERS', 1000)),
        'dry_run': (os.environ.get('DRY_RUN', 'true') == 'true'),
        'user_slack_token': os.environ.get('USER_SLACK_TOKEN', ''),
        'bot_slack_token': os.environ.get('BOT_SLACK_TOKEN', ''),
        'too_old_datetime': (datetime.now() - timedelta(days=days_inactive)),
        'whitelist_keywords': os.environ.get('WHITELIST_KEYWORDS', ''),
        'skip_subtypes': {'channel_leave', 'channel_join'},
        'skip_channel_str': os.environ.get('SLACK_SKIP_PURPOSE', 'noarchive'),
    }
