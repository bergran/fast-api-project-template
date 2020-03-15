# -*- coding: utf-8 -*-
import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship

from core.db.base import metadata

App = Table(
    'App',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(254)),
    Column("created", DateTime, default=datetime.datetime.utcnow),
    Column("modified", DateTime, default=datetime.datetime.utcnow),
    Column("client_id", String(36), default=uuid4),
    Column("client_secret", String(36), default=uuid4),
    Column("access_tokens", Integer, ForeignKey('AccessToken.id')),
)

App.access_tokens = relationship('AccessToken')
