# -*- coding: utf-8 -*-
import logging

from flask_restplus import Resource

from family_tree.database import get_siblings
from .namespace import ns
from .serializers import person_model
from ..restplus import api

log = logging.getLogger(__name__)


@ns.route('/<string:id>/siblings')
@api.response(404, 'Person not found.')
class PersonSiblings(Resource):
    @api.marshal_with(person_model)
    def get(self, id: str):
        """siblings of person"""
        db = ns.db.session()
        persons = get_siblings(db, id)
        if persons is None:
            return None, 404
        return persons
