# -*- coding: utf-8 -*-
import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY


from core.db.base import Base


class AccessToken(Base):
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    modified = Column(DateTime, default=datetime.datetime.utcnow)
    app = Column(Integer, ForeignKey('app.id'))
    scopes = Column(ARRAY(String), default=[])
    access_token = Column(String(36), default=uuid4)
