#  -*- coding: utf-8 -*-

import re

from fastapi import Header, HTTPException
from starlette import status
from starlette.requests import Request

from apps.token.constants.jwt import JWT_REGEX


def get_jwt(request: Request, authorization: str = Header('', alias='Authorization')) -> str:
    config = request.state.config

    regex = JWT_REGEX.format(config.JWT_AUTH_HEADER_PREFIX)

    if not re.match(regex, authorization):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Authorization has wrong format")

    return authorization.split(' ')[-1]
