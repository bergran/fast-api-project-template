# -*- coding: utf-8 -*-

from fastapi.routing import APIRouter

from apps.health_check.urls import router as router_health_check
from apps.hello_world.urls import router as router_hello_world
from apps.token.urls import router as router_token
from apps.oauth2.urls import router as router_oauth2


router = APIRouter()
router.include_router(router_health_check, prefix='/api/v1', tags=['health_check'])
router.include_router(router_hello_world, prefix='/api/v1', tags=['hello_work'])
router.include_router(router_token, prefix='/api/v1', tags=['token'])
router.include_router(router_oauth2, prefix='/api/v1', tags=['oauth2'])
