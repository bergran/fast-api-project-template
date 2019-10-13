# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.utils.init_db import get_dsn


def setup_database(app_config):
    dsn = get_dsn(app_config)
    engine = create_engine(dsn)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session, dsn
