# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

from .person_crud import (
    get_all_persons,
    get_person,
    get_siblings,
    get_parents, get_children,
    get_grandparents, get_cousins,
)

db = SQLAlchemy()

__all__ = [
    db,
    get_all_persons, get_person,
    get_siblings, get_parents, get_children,
    get_grandparents, get_cousins,
]
