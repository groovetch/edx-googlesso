import logging
import urllib2
import json
import wget
from django.utils.timezone import now
from openedx.core.djangoapps.profile_images.images import create_profile_images
from openedx.core.djangoapps.profile_images.views import _make_upload_dt
from openedx.core.djangoapps.user_api.accounts.image_helpers import get_profile_image_names, set_has_profile_image


log = logging.getLogger(__name__)


def download_google_profile_image(auth_entry, strategy, details, user=None, *args, **kwargs):
    if user and not user.profile.profile_image_uploaded_at:
        try:
            username = user.username
            req = urllib2.Request('https://people.googleapis.com/v1/people/me?personFields=photos')
            req.add_header('Authorization', 'Bearer {0}'.format(kwargs['response']['access_token']))
            resp = urllib2.urlopen(req)
            content = json.loads(resp.read())
            image_filename = wget.download(content["photos"][0]["url"])
            profile_image_names = get_profile_image_names(user.username)
            create_profile_images(image_filename, profile_image_names)
            set_has_profile_image(username, True, _make_upload_dt())
            user.profile.profile_image_uploaded_at = now()
            user.save()

        except Exception as e:
            log.exception('Error when downloading user image from Google API', exc_info=True)
