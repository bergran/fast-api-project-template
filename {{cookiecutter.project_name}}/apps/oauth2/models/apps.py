# -*- coding: utf-8 -*-
import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from core.db.base import Base


class App(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(254))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    modified = Column(DateTime, default=datetime.datetime.utcnow)
    client_id = Column(String(36), default=uuid4)
    client_secret = Column(String(36), default=uuid4)

    access_tokens = relationship('AccessToken')
