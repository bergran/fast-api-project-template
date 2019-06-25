# -*- coding: utf-8 -*-

from fastapi.routing import APIRouter
from apps.health_check.views.health_check import router as router_health_check


router = APIRouter()
router.include_router(router_health_check, prefix='/health-check')
