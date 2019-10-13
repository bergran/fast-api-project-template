# -*- coding: utf-8 -*-

from fastapi.routing import APIRouter
from apps.oauth2.views.token_access import router as router_token_access
from apps.oauth2.views.view_protected import router as router_protected

router = APIRouter()

router.include_router(router_token_access)
router.include_router(router_protected)
