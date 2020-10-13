"""
App configuration for google_picture_profile.
"""

from __future__ import unicode_literals

from django.apps import AppConfig
from django.conf import settings


class GooglePictureProfileConfig(AppConfig):
    """
    google_picture_profile configuration.
    """
    name = 'google_picture_profile'
    verbose_name = 'google_picture_profile'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'google_picture_profile',
                'regex': r'^google_picture_profile/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': 'google_picture_profile',
                'regex': r'^google_picture_profile/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
        }
    }
    def ready(self):
        if settings.FEATURES.get('ENABLE_GOOGLE_PICTURE_PROFILE', False):
            if settings.FEATURES.get('ENABLE_THIRD_PARTY_AUTH', False):
                settings.SOCIAL_AUTH_PIPELINE += [
                    'google_picture_profile.pipeline.download_google_profile_image',
                ]
