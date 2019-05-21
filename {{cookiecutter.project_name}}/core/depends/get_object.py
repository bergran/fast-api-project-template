# -*- coding: utf-8 -*-
from fastapi import Path, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from core.db.base import Base
from core.depends import get_database


def get_object(model: Base, pk: str):
    def wrap(
            obj_pk: int = Path(..., alias = pk),
            db: Session = Depends(get_database)
    ):
        obj = db.query(model).filter(getattr(model, pk) == obj_pk).first()
        if obj is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

        return obj

    return wrap
