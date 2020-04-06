# -*- coding: utf-8 -*-
"""
relation DTO model
"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from . import Base


class RelationDto(Base):
    __tablename__ = 'relations'

    parent_id = Column(UUID(as_uuid=True), ForeignKey('persons.id'), primary_key=True)
    relation_type = Column(Integer)
    child_id = Column(UUID(as_uuid=True), ForeignKey('persons.id'))
