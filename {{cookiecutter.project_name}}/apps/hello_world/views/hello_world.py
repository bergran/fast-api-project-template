# -*- coding: utf-8 -*-


from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/")
async def hello_world():
    return {"message": "Hello World"}
