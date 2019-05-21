# -*- coding: utf-8 -*-
import jwt
from fastapi import Depends, HTTPException
from starlette import status
from starlette.requests import Request

from apps.token.depends.get_jwt import get_jwt


def get_token_decoded(request: Request, jwt_token: str = Depends(get_jwt)) -> str:
    config = request.state.config

    try:
        token = jwt.decode(jwt_token, config.JWT_SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ex))
    except jwt.InvalidSignatureError as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ex))

    return token
