# -*- coding: utf-8 -*-
from fastapi import Depends, Header
from sqlalchemy import cast, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Session, aliased

from apps.oauth2.models import App, AccessToken
from apps.oauth2.serializers.token_access import TokenAccess
from core.depends import get_database
from core.utils.get_object_or_404 import get_object_or_404


def get_app_object_access(session: Session = Depends(get_database), access: TokenAccess = Depends()):
    return get_object_or_404(session.query(App).filter(
        App.client_secret == access.client_secret,
        App.client_id == access.client_id
    ))


def get_app_object_scopes(scopes):
    def wrapper(session: Session = Depends(get_database), authorization: str = Header(..., alias='Authorization')):
        _, authorization_splited = authorization.split(' ')
        return get_object_or_404(session.query(App).join(AccessToken).filter(
            AccessToken.access_token == authorization_splited,
            AccessToken.scopes.contains(cast(scopes, ARRAY(String)))
        ))

    return wrapper
