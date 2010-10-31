# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy import Rule

rules = [
    Rule('/', name='index', handler='milsalumni.handlers.IndexHandler'),
]
