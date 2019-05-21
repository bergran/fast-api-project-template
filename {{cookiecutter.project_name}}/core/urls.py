# -*- coding: utf-8 -*-

from fastapi.routing import APIRouter

from apps.hello_world.urls import router as router_hello_world
from apps.token.urls import router as router_token

router = APIRouter()
router.include_router(router_hello_world, prefix='/api/v1', tags=['hello_world'])
router.include_router(router_token, prefix='/api/v1', tags=['token'])
