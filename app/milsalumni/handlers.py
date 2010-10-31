# -*- coding: utf-8 -*-

from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

from middleware import ChromeFrameMiddleware

class PageRequestHandler(RequestHandler, Jinja2Mixin):	
	middleware = [ChromeFrameMiddleware()]

class IndexHandler(PageRequestHandler):
    def get(self):
        return self.render_response('index.html', message="Hello world")
