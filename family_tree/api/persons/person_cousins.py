# -*- coding: utf-8 -*-
import logging

from flask_restplus import Resource

from family_tree.database import get_cousins
from .namespace import ns
from .serializers import person_model
from ..restplus import api

log = logging.getLogger(__name__)


@ns.route('/<string:id>/cousins')
@api.response(404, 'Person not found.')
class PersonCousins(Resource):
    @api.marshal_with(person_model)
    def get(self, id: str):
        """cousins of person"""
        db = ns.db.session()
        persons = get_cousins(db, id)
        if persons is None:
            return None, 404
        return persons
