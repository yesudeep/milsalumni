# -*- coding: utf-8 -*-
"""App configuration."""

# Make this false before deploying on production.
DEBUG = True
#DEBUG = False

APPLICATION_TITLE = 'MILS Alumni'
CSS_URL = '/css/'
JS_URL = '/js/'
IMAGE_URL = '/image/'

JS_MINIFICATION_SUFFIX = '.min.js'
CSS_MINIFICATION_SUFFIX = '.min.css'

config = {}

config['tipfy'] = {
	'auth_store_class': 'tipfy.auth.MultiAuthStore',
	'enable_debugger': DEBUG,
}
