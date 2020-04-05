# -*- coding: utf-8 -*-
"""
person DTO model
"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from . import Base


class PersonDto(Base):
    __tablename__ = 'persons'

    id = Column(UUID(as_uuid=True), primary_key=True)
    firstname = Column(String(150), nullable=False)
    lastname = Column(String(150), nullable=False)
    phone = Column(String(15))
    email = Column(String(100))
    birthdate = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Person(Name='{self.firstName} {self.lastName}' id='{self.id}')>"
