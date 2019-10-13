#  -*- coding: utf-8 -*-
from fastapi import Header, HTTPException
from starlette import status


def get_remote_host(
        host: str = Header(None),
        x_real_ip: str = Header(None, alias='X-Real-IP'),
        scheme: str = Header('http')
):
    template_host = '{}://{}'
    if x_real_ip:
        return template_host.format(scheme, x_real_ip)
    elif host:
        return template_host.format(scheme, host)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='X-Real-Ip header is not set')
