# -*- coding: utf-8 -*-

from fastapi import Form
from pydantic import BaseModel


class TokenAccess:

    def __init__(
            self,
            grant_type: str = Form(..., regex="^client_credentials$"),
            scope: str = Form(''),
            client_id: str = Form(None),
            client_secret: str = Form(None),
    ):
        self.grant_type = grant_type
        self.scopes = scope.split()
        self.client_id = client_id
        self.client_secret = client_secret


class TokenOut(BaseModel):
    access_token: str
    token_type: str
