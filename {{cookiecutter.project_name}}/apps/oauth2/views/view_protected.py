# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from apps.oauth2.depends.app import get_app_object_scopes
from apps.oauth2.models import App
from apps.oauth2.serializers.app import AppOut

router = APIRouter()


@router.get('/me', response_model=AppOut)
def me(app: App = Depends(get_app_object_scopes(['me']))):
    return jsonable_encoder(app)
