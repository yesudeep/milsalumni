# -*- coding: utf-8 -*-
"""App configuration."""

from secrets import secret_key
from tipfy.app import APPENGINE, DEV_APPSERVER

# Make this false before deploying on production.
DEBUG = True
#DEBUG = False

GOOGLE_ANALYTICS_ID = 'UA-7340598-3'

JS_URL = '/js/'
CSS_URL = '/css/'
IMAGE_URL = '/i/'

HTML5RESET_VERSION = '1.6.1'
JQUERY_VERSION = '1.4.3'

if DEV_APPSERVER:
	JQUERY_URL = JS_URL + 'vendor/jquery-%s.min.js' % JQUERY_VERSION
	ANALYTICS_CODE = ''
	FONTS_CODE = ''
        HTML5RESET_CSS_URL = CSS_URL + 'html5reset-%s.css' % HTML5RESET_VERSION
else:
	JQUERY_URL = 'http://ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js' % JQUERY_VERSION
	ANALYTICS_CODE = """<script type="text/javascript">var _gaq=_gaq||[];_gaq.push(['_setAccount', '%(GOOGLE_ANALYTICS_ID)s']);_gaq.push(['_trackPageview']);(function(){var doc=document,ga=doc.createElement('script');ga.src=('https:'==doc.location.protocol?'https://ssl':'http://www')+'.google-analytics.com/ga.js';ga.setAttribute('async', 'true');doc.documentElement.firstChild.appendChild(ga);})();</script>""" % dict(GOOGLE_ANALYTICS_ID=GOOGLE_ANALYTICS_ID)
	FONTS_CODE = '''
	<link href='http://fonts.googleapis.com/css?family=Philosopher|Cuprum|Droid+Serif:regular,italic,bold,bolditalic&subset=latin' rel='stylesheet' type='text/css'>
	'''
        HTML5RESET_CSS_URL = 'http://html5resetcss.googlecode.com/files/html5reset-%s.css' % HTML5RESET_VERSION

meta_config = dict(
	APPLICATION_TITLE='MILS Alumni',
	CSS_URL=CSS_URL,
	JS_URL=JS_URL,
	IMAGE_URL=IMAGE_URL,
	JS_MINIFICATION_SUFFIX='.min.js',
	CSS_MINIFICATION_SUFFIX='.min.css',
	JQUERY_URL=JQUERY_URL,
	ANALYTICS_CODE=ANALYTICS_CODE,
	FONTS_CODE=FONTS_CODE,
        HTML5RESET_CSS_URL=HTML5RESET_CSS_URL,
)


config = {}

config['tipfy'] = {
	'auth_store_class': 'tipfy.auth.MultiAuthStore',
	'enable_debugger': DEBUG,
        'session_store_class': 'tipfy.sessions.SecureCookieStore',
        }
config['tipfy.sessions'] = {
        'secret_key': secret_key,
        }
