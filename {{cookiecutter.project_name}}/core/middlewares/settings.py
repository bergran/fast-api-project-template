# -*- coding: utf-8 -*-
from starlette.requests import Request
from starlette.responses import Response

from core.utils.init_config import init_config


def settings_middleware(app):
    config_obj = init_config()

    if config_obj.SECRET_KEY is None:
        raise RuntimeError('You have to set SECRET_KEY in the config module')

    app.config = config_obj

    async def settings_add_app(request: Request, call_next):
        response = Response("Internal server error", status_code=500)
        try:
            request.state.config = config_obj
            response = await call_next(request)
        finally:
            pass
        return response

    return settings_add_app
