# -*- coding: utf-8 -*-
from fastapi import HTTPException
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from starlette import status


def get_object_or_404(qs):
    try:
        return qs.one()
    except MultipleResultsFound:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
