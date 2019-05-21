# -*- coding: utf-8 -*-
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from starlette.responses import Response

from core.utils.init_db import get_dsn


def database_middleware(app):
    dsn = get_dsn(app.config)
    app_config = app.config

    engine = create_engine(dsn)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

    app_config.SQLALCHEMY_DATABASE_URI = dsn

    async def db_session_middleware(request: Request, call_next):
        response = Response("Internal server error", status_code=500)
        try:
            request.state.db = session
            response = await call_next(request)
        finally:
            request.state.db.rollback()
            request.state.db.close()
        return response

    return db_session_middleware
