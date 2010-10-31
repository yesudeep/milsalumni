# -*- coding: utf-8 -*-

import config
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

from middleware import ChromeFrameMiddleware, TemplateContextMiddleware

template_context_middleware = TemplateContextMiddleware(
	DEBUG=config.DEBUG,
	APPLICATION_TITLE=config.APPLICATION_TITLE,
	CSS_URL=config.CSS_URL,
	IMAGE_URL=config.IMAGE_URL,
	JS_URL=config.JS_URL,
	JS_MINIFICATION_SUFFIX=config.JS_MINIFICATION_SUFFIX,
	CSS_MINIFICATION_SUFFIX=config.CSS_MINIFICATION_SUFFIX,
	)

class PageRequestHandler(RequestHandler, Jinja2Mixin):
	middleware = [ChromeFrameMiddleware(), template_context_middleware]

class IndexHandler(PageRequestHandler):
    def get(self):
        #return self.render_response('index.html', message="Hello world")

		return Response(str(self.context))

