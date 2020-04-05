# -*- coding: utf-8 -*-
import logging
import sys

from flask import (
    current_app,
    jsonify,
)
from flask_restplus import Resource
from sqlalchemy import text

from ..restplus import api

log = logging.getLogger(__name__)
ns = api.namespace('app', description='Application Information')


@ns.route('/version')
class AppVersion(Resource):
    @api.response(200, 'Application is running')
    def get(self):
        """return application version"""
        title = current_app.config['APP_NAME']
        ver = current_app.config['VERSION']
        return jsonify({'title': title, 'version': ver})


@ns.route('/readiness')
class AppRediness(Resource):
    @api.response(200, 'Application is ready')
    @api.response(503, 'db is not available')
    def get(self):
        """check db connectivity"""
        try:
            db = ns.db.session()
            db.execute(text("SELECT 1"))
        except:
            log.error("Unexpected error:", sys.exc_info()[0])
            return 'db connection error', 503
        return 'OK'
