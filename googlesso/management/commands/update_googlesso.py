from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand
import logging

GOOGLE_CLIENT_ID=settings.GOOGLE_CLIENT_ID
log = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Updating Client ID for Google'


    def handle(self, *args, **options):
        try:
            OAuth2ProviderConfig = apps.get_model('third_party_auth', 'OAuth2ProviderConfig')
            google_oauth = OAuth2ProviderConfig.objects.filter(name='Google').latest('id')
            if google_oauth.key == "":
                google_oauth.key = GOOGLE_CLIENT_ID
                google_oauth.save()
                self.stdout.write(self.style.SUCCESS('Updated Provider Configuration (OAuth) for Google with key %s' % GOOGLE_CLIENT_ID))
            else:
                self.stdout.write(self.style.WARNING('Exist Client ID: %s' % google_oauth.key))
        except Exception as e:
            log.exception('Error when updating Client ID from Google', exc_info=True)
