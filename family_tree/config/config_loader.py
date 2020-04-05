# -*- coding: utf-8 -*-
import os
import logging.config

from flask.config import Config
from .default_config import DefaultConfig


log = logging.getLogger(__name__)


def init_config(config: Config) -> None:
    """Load config"""
    env_flask_config_name = os.getenv('FLASK_CONFIG') or 'development'
    flask_config_name = f'config.{env_flask_config_name}.json'
    config.from_object(DefaultConfig())
    config.from_json(os.path.normpath(os.path.join(os.path.dirname(__file__), flask_config_name)))
    config.from_envvar('SQLALCHEMY_DATABASE_URI', True)
    config.from_envvar('APP_VERSION', True)
    config.from_envvar('SERVER_NAME', True)
