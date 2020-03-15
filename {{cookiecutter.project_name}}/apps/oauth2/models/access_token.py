# -*- coding: utf-8 -*-
import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.dialects.postgresql import ARRAY

from core.db.base import metadata


AccessToken = Table(
    'AccessToken',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("created", DateTime, default=datetime.datetime.utcnow),
    Column("modified", DateTime, default=datetime.datetime.utcnow),
    Column("app", Integer, ForeignKey('App.id')),
    Column("scopes", ARRAY(String), default=[]),
    Column("access_token", String(36), default=uuid4),
)
