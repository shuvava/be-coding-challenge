# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_restplus import Resource

from family_tree.database import (
    get_all_persons
)
from .namespace import ns
from .parsers import pagination_arguments
from .serializers import person_model
from ..restplus import api

log = logging.getLogger(__name__)


@ns.route('/')
class PersonsCollection(Resource):
    @api.expect(pagination_arguments)
    @api.marshal_with(person_model)
    def get(self):
        """collection of persons"""
        args = pagination_arguments.parse_args(request)
        skip = args.get('skip', 0)
        limit = args.get('limit', 100)
        sort_column = args.get('sort_column', '')
        sort_dir = args.get('sort_dir', 'asc')

        db = ns.db.session()
        persons = get_all_persons(db, skip, limit, sort_column, sort_dir)

        return persons
