# -*- coding: utf-8 -*-
from typing import List

from sqlalchemy import desc, asc
from sqlalchemy.orm import Session

from .models.person import Person
from .models.person_dto import PersonDto


def get_all_persons(db: Session, skip: int = 0, limit: int = 100, sort_column: str = '', sort_dir: str = 'asc') -> List[
    Person]:
    if sort_column:
        sort = asc(sort_column) if sort_dir == 'desc' else desc(sort_column)
        return db.query(PersonDto).order_by(sort).offset(skip).limit(limit).all()
    items = db.query(PersonDto).offset(skip).limit(limit).all()
    return [mapper_from_dto(item) for item in items]


def get_person(db: Session, id: str) -> Person:
    db.execute('SET search_path TO dbo')
    item = db.query(PersonDto).filter(PersonDto.id == id).first()
    return mapper_from_dto(item)


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
