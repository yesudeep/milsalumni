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


class TemplateContextMiddleware(object):
	"""
		Middleware that adds a few template context defaults.
	"""

	def __init__(self, **context):
		self.context = context

	def before_dispatch(self, handler):
		handler.context.update(self.context)
