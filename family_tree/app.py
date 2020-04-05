# -*- coding: utf-8 -*-
import logging.config

from flask import Flask, Blueprint
from flask_cors import CORS

from family_tree.api import (
    api,
    app_version_ns, persons_ns
)
from family_tree.config import init_config
from family_tree.database import db

log = logging.getLogger(__name__)


def configure_app(app: Flask) -> None:
    init_config(app.config)
    CORS(app)


def initialize_app(app: Flask) -> None:
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    db.init_app(app)
    api.init_app(app)

    app_version_ns.db = db
    api.add_namespace(app_version_ns)
    persons_ns.db = db
    api.add_namespace(persons_ns)


def create_app() -> Flask:
    app = Flask(__name__)

    configure_app(app)
    initialize_app(app)
    log.info('>>>>>> application started <<<<<<<')

    return app
