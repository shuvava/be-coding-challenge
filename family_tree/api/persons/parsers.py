# -*- coding: utf-8 -*-
from flask_restplus import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('skip', type=int, required=False, default=0, help='skip number of elements')
pagination_arguments.add_argument('limit', type=int, required=False, choices=[2, 10, 20, 30, 40, 50, 100], default=100,
                                  help='results per page')
pagination_arguments.add_argument('sort_column', type=str, required=False, choices=['firstName', 'lastName'],
                                  default='', help='filed to sort result')
pagination_arguments.add_argument('sort_dir', type=str, required=False, choices=['asc', 'desc'],
                                  default='asc', help='sort direction')
