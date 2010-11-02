# -*- coding: utf-8 -*-

import config
from config import meta_config
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin
from middleware import ChromeFrameMiddleware, TemplateContextMiddleware

template_context = dict(DEBUG=config.DEBUG)
template_context.update(meta_config)
template_context_middleware = TemplateContextMiddleware(**template_context)

class PageRequestHandler(RequestHandler, Jinja2Mixin):
	middleware = [ChromeFrameMiddleware(), template_context_middleware]

class IndexHandler(PageRequestHandler):
    def get(self):
        return self.render_response('index.html', **self.context)
