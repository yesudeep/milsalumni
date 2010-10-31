# -*- coding: utf-8 -*-
"""
Middleware classes for the application.
"""


class ChromeFrameMiddleware(object):
	"""
		Middleware that enables the Google Chrome Frame plugin.
	"""
	def after_dispatch(self, handler, response):
		response.headers.add('X-UA-Compatible', 'chrome=1')
		return response
