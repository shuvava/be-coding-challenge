#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
import logging.config
import os

log_config_name = os.getenv('LOGGING_CONFIG') or 'logging.conf'
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), f'family_tree/config/{log_config_name}'))
logging.config.fileConfig(logging_conf_path)

from family_tree.app import create_app
from family_tree.middleware import monitor


def run_app():
    app = create_app()
    monitor(app)
    app.run()


if __name__ == '__main__':
    run_app()
