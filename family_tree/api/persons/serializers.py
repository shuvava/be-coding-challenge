# -*- coding: utf-8 -*-
from flask_restplus import fields

from ..restplus import api

person_model = api.model('Person', {
    'id': fields.String(readOnly=True, description='The unique identifier of a person'),
    'firstName': fields.String(required=True, description='First Name'),
    'lastName': fields.String(required=True, description='Last Name'),
    'phone': fields.String(required=False, description='Phone'),
    'email': fields.String(required=False, description='Email'),
    'birthDate': fields.DateTime,
})
