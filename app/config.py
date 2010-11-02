# -*- coding: utf-8 -*-
"""App configuration."""

from tipfy.app import APPENGINE, DEV_APPSERVER

# Make this false before deploying on production.
DEBUG = True
#DEBUG = False

GOOGLE_ANALYTICS_ID = 'UA-7340598-3'

JS_URL = '/js/'
if DEV_APPSERVER:
	JQUERY_URL = JS_URL + 'vendor/jquery-1.4.3.min.js'
	ANALYTICS_CODE = ''
else:
	JQUERY_URL = 'http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js'
	ANALYTICS_CODE = """<script type="text/javascript">var _gaq=_gaq||[];_gaq.push(['_setAccount', '%(GOOGLE_ANALYTICS_ID)s']);_gaq.push(['_trackPageview']);(function(){var doc=document,ga=doc.createElement('script');ga.src=('https:'==doc.location.protocol?'https://ssl':'http://www')+'.google-analytics.com/ga.js';ga.setAttribute('async', 'true');doc.documentElement.firstChild.appendChild(ga);})();</script>""" % dict(GOOGLE_ANALYTICS_ID=GOOGLE_ANALYTICS_ID)

meta_config = dict(
	APPLICATION_TITLE = 'MILS Alumni',
	CSS_URL='/css/',
	JS_URL=JS_URL,
	IMAGE_URL='/image/',
	JS_MINIFICATION_SUFFIX='.min.js',
	CSS_MINIFICATION_SUFFIX='.min.css',
	JQUERY_URL=JQUERY_URL,
	ANALYTICS_CODE=ANALYTICS_CODE,
)

config = {}

config['tipfy'] = {
	'auth_store_class': 'tipfy.auth.MultiAuthStore',
	'enable_debugger': DEBUG,
}
