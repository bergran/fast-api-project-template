# -*- coding: utf-8 -*-

from starlette.requests import Request
from starlette.responses import Response

from core.db.setup import setup_database


def database_middleware(app):
    app_config = app.config
    session, dsn = setup_database(app_config)

    app_config.SQLALCHEMY_DATABASE_URI = dsn

    async def db_session_middleware(request: Request, call_next):
        response = Response("Internal server error", status_code=500)
        try:
            request.state.db = session()
            response = await call_next(request)
        finally:
            request.state.db.rollback()
            request.state.db.close()
        return response

    return db_session_middleware
