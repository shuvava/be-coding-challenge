# -*- coding: utf-8 -*-
from .app.app_version import ns as app_version_ns
from .persons import ns as persons_ns
from .restplus import api

__all__ = [
    api,
    app_version_ns,
    persons_ns,
]
