# -*- coding: utf-8 -*-
import logging
from typing import List

from flask import current_app
from sqlalchemy import desc, asc
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Session

from .models.person import Person
from .models.person_dto import PersonDto
from .models.relation_dto import RelationDto

log = logging.getLogger(__name__)

def get_all_persons(db: Session, skip: int = 0, limit: int = 100, sort_column: str = '', sort_dir: str = 'asc') -> List[
    Person]:
    if sort_column:
        sort = asc(sort_column) if sort_dir == 'desc' else desc(sort_column)
        return db.query(PersonDto).order_by(sort).offset(skip).limit(limit).all()
    items = db.query(PersonDto).offset(skip).limit(limit).all()
    return [mapper_from_dto(item) for item in items]


def get_person(db: Session, id: str) -> Person:
    # db.execute('SET search_path TO dbo')
    item = db.query(PersonDto).filter(PersonDto.id == id).first()
    return mapper_from_dto(item)


def get_siblings(db: Session, id: str, skip: int = 0, limit: int = 100) -> List[Person]:
    father = db.query(RelationDto) \
        .filter(RelationDto.relation_type == 2) \
        .filter(RelationDto.parent_id == id) \
        .subquery()
    siblings = db.query(RelationDto) \
        .join(father, RelationDto.parent_id == father.c.child_id) \
        .filter(RelationDto.relation_type == 1) \
        .subquery()
    items = db.query(PersonDto) \
        .join(siblings, PersonDto.id == siblings.c.child_id) \
        .filter(PersonDto.id != id) \
        .offset(skip).limit(limit).all()
    return [mapper_from_dto(item) for item in items]


def get_parents(db: Session, id: str, skip: int = 0, limit: int = 100) -> List[Person]:
    father = db.query(RelationDto) \
        .filter(RelationDto.relation_type == 2) \
        .filter(RelationDto.parent_id == id) \
        .subquery()
    items = db.query(PersonDto) \
        .join(father, PersonDto.id == father.c.child_id) \
        .offset(skip).limit(limit).all()
    return [mapper_from_dto(item) for item in items]


def get_children(db: Session, id: str, skip: int = 0, limit: int = 100) -> List[Person]:
    children = db.query(RelationDto) \
        .filter(RelationDto.relation_type == 1) \
        .filter(RelationDto.parent_id == id) \
        .subquery()
    query = db.query(PersonDto) \
        .join(children, PersonDto.id == children.c.child_id) \
        .offset(skip).limit(limit)
    if current_app.debug:
        log.info(query.statement.compile(dialect=postgresql.dialect()))
    items = query.all()
    return [mapper_from_dto(item) for item in items]


def get_grandparents(db: Session, id: str, skip: int = 0, limit: int = 100) -> List[Person]:
    father = db.query(RelationDto) \
        .filter(RelationDto.relation_type == 2) \
        .filter(RelationDto.parent_id == id) \
        .subquery()
    grandparents = db.query(RelationDto) \
        .join(father, RelationDto.parent_id == father.c.child_id) \
        .filter(RelationDto.relation_type == 2) \
        .subquery()
    items = db.query(PersonDto) \
        .join(grandparents, PersonDto.id == grandparents.c.child_id) \
        .offset(skip).limit(limit).all()
    return [mapper_from_dto(item) for item in items]


def get_cousins(db: Session, id: str, skip: int = 0, limit: int = 100) -> List[Person]:
    father = db.query(RelationDto) \
        .filter(RelationDto.relation_type == 2) \
        .filter(RelationDto.parent_id == id) \
        .subquery()
    grandparents = db.query(RelationDto) \
        .join(father, RelationDto.parent_id == father.c.child_id) \
        .filter(RelationDto.relation_type == 2) \
        .subquery()
    fathers = db.query(RelationDto) \
        .join(grandparents, RelationDto.parent_id == grandparents.c.child_id) \
        .filter(RelationDto.relation_type == 1) \
        .subquery()
    cousins = db.query(RelationDto) \
        .join(fathers, RelationDto.parent_id == fathers.c.child_id) \
        .filter(RelationDto.relation_type == 1) \
        .subquery()
    items = db.query(PersonDto) \
        .join(cousins, PersonDto.id == cousins.c.child_id) \
        .filter(PersonDto.id != id) \
        .offset(skip).limit(limit).all()
    return [mapper_from_dto(item) for item in items]


def mapper_from_dto(item: PersonDto) -> Person:
    if item is None:
        return None
    person = Person()
    person.id = item.id
    person.lastName = item.lastname
    person.firstName = item.firstname
    person.phone = item.phone
    person.email = item.email
    person.birthDate = item.birthdate

    return person
