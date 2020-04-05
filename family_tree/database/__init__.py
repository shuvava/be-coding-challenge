# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

from .person_crud import (
    get_all_persons,
    get_person
)

db = SQLAlchemy()

__all__ = [
    db,
    get_all_persons, get_person,
]
