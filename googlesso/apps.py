"""
App configuration for googlesso.
"""

from __future__ import unicode_literals

from django.apps import AppConfig
from django.conf import settings


class GoogleSSOConfig(AppConfig):
    """
    googlesso configuration.
    """
    name = 'googlesso'
    verbose_name = 'googlesso'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'googlesso',
                'regex': r'^googlesso/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': 'googlesso',
                'regex': r'^googlesso/',
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
                    'googlesso.picture_profile.pipeline.download_google_profile_image',
                ]
