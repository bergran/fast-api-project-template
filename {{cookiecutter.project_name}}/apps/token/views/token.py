# -*- coding: utf-8 -*-
from fastapi import Depends
from fastapi.routing import APIRouter
from starlette import status

from apps.token.depends.get_jwt import get_jwt
from apps.token.depends.get_token_decode import get_token_decoded
from core.serializers.message import Message

router = APIRouter()


@router.post('/verify-token', status_code=status.HTTP_200_OK, responses={400: {"model": Message}})
def verify_token(token: str = Depends(get_token_decoded), jwt_token: str = Depends(get_jwt)):
    return {'token': jwt_token}
