# -*- coding: utf-8 -*-

from fastapi.routing import APIRouter

from apps.token.views.token import router as router_token


router = APIRouter()
router.include_router(router_token)