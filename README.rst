======================
google_picture_profile
======================


Features
########

This plugin is to download and set user profile picture from GOOGLE API

Usage
#####

Note: socialoauth plugin is required.

Following command bellow to install google_picture_profile:
- Run `grvlms plugins enable socialoauth`
- Run `grvlms socialoauth config -i`:
    - Set ENABLE_GOOGLE_PICTURE_PROFILE: true and make sure SOCIALOAUTH_ACTIVATE_GOOGLE: true
    - Input value in SOCIALOAUTH_GOOGLE_CLIENT_ID and SOCIALOAUTH_GOOGLE_SECRET_KEY
- Run `grvlms socialoauth init`
