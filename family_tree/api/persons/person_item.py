# -*- coding: utf-8 -*-
import logging

from flask_restplus import Resource

from family_tree.database import get_person
from .namespace import ns
from .serializers import person_model
from ..restplus import api

log = logging.getLogger(__name__)


@ns.route('/<string:id>')
@api.response(404, 'Person not found.')
class PersonsItem(Resource):
    @api.marshal_with(person_model)
    def get(self, id: str):
        """person by id"""
        db = ns.db.session()
        person = get_person(db, id)
        if person is None:
            return None, 404
        return person
