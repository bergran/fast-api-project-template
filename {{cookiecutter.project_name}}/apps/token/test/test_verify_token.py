# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta

import jwt
from starlette import status

from core import config
from core.test.transaction_test_case import TransactionTestCase


class VerifyTokenTestCase(TransactionTestCase):

    def setUp(self):
        self.token_good = self.generate_jwt(datetime.utcnow() + timedelta(minutes=30), config.SECRET_KEY)
        self.token_expired = self.generate_jwt(datetime.utcnow() - timedelta(minutes=30), config.SECRET_KEY)
        self.token_with_other_sign = self.generate_jwt(datetime.utcnow(), 'Im not secret key :)')

    def generate_jwt(self, exp_time, secret):
        return jwt.encode(
            {'message': 'hello world', 'exp': exp_time}, secret
        )

    def test_with_good_token(self):
        token = self.token_good.decode('utf-8')

        response = self.client.post('api/v1/verify-token', headers={
            'Authorization': '{} {}'.format(config.JWT_AUTH_HEADER_PREFIX, token)
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'token': token})

    def test_with_token_expired(self):
        token = self.token_expired.decode('utf-8')

        response = self.client.post('api/v1/verify-token', headers={
            'Authorization': '{} {}'.format(config.JWT_AUTH_HEADER_PREFIX, token)
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_with_other_sign(self):
        token = self.token_with_other_sign.decode('utf-8')

        response = self.client.post('api/v1/verify-token', headers={
            'Authorization': '{} {}'.format(config.JWT_AUTH_HEADER_PREFIX, token)
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_authentication_header(self):
        self.assertIsNotNone(self.session)
        response = self.client.post('api/v1/verify-token')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
