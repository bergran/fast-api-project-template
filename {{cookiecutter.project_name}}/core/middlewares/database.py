# -*- coding: utf-8 -*-

from starlette.requests import Request
from starlette.responses import Response


def database_middleware(app):
    async def db_session_middleware(request: Request, call_next):
        response = Response("Internal server error", status_code=500)
        transaction = await app.database.transaction()
        try:
            request.state.db = transaction
            response = await call_next(request)
        except Exception:
            transaction.rollback()
        else:
            transaction.commit()
        return response

    return db_session_middleware
