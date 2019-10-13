#  -*- coding: utf-8 -*-

from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette import status

from apps.oauth2.depends.app import get_app_object_access
from apps.oauth2.models.access_token import AccessToken
from apps.oauth2.models.apps import App
from apps.oauth2.serializers.token_access import TokenAccess, TokenOut
from core.config import SCOPES
from core.depends import get_database

router = APIRouter()


@router.post('/token', response_model=TokenOut)
async def login_for_access_token(app: App = Depends(get_app_object_access),
                                 session: Session = Depends(get_database),
                                 access: TokenAccess = Depends()):
    scopes = access.scopes

    if len(scopes) == 0:
        scopes = [list(SCOPES.keys())[0]]

    allowed_scopes = SCOPES.keys()

    for scope in scopes:
        if scope not in allowed_scopes:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail={'scope': f'{scope} scope is not in allowed scopes'})

    access_token = AccessToken(scopes=scopes)
    app.access_tokens.append(access_token)
    session.commit()

    return {"access_token": access_token.access_token, "token_type": "bearer"}
