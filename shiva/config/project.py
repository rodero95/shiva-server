# -*- coding: utf-8 -*-
from shiva.converter import Converter

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///shiva.db'
ACCEPTED_FORMATS = (
    'mp3',
)
CONVERTER_CLASS = Converter
MIMETYPES = {
    'audio': {
        'audio/mp3': {
            'codec': 'libmp3lame',
            'extension': 'mp3'
        },
        'audio/ogg': {
            'acodec': 'libvorbis',
            'extension': 'ogg'
        },
    },
}
DEFAULT_ALBUM_COVER = ('http://wortraub.com/wp-content/uploads/2012/07/'
                       'Vinyl_Close_Up.jpg')
DEFAULT_ARTIST_IMAGE = 'http://www.super8duncan.com/images/band_silhouette.jpg'

# https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
CORS_ENABLED = False
# CORS_ALLOWED_ORIGINS accepts the following values:
# The string '*' to allow all origins
# An specific domain: 'google.com'
# A tuple of strings to allow multiple domains: ('google.com', 'napster.com')
CORS_ALLOWED_ORIGINS = '*'
