# -*- coding: utf-8 -*-

from starlette import status

from apps.oauth2.models import App, AccessToken
from core.test.transaction_test_case import TransactionTestCase
from core.utils.get_object_or_404 import get_object


class AccessTokenTestCase(TransactionTestCase):

    def setUp(self):
        session = self.session

        self.app_model = App(name='App test')
        session.add(self.app_model)
        session.commit()

    def test_send_json(self):
        body = {
            'client_id': self.app_model.client_id,
            'client_secret': self.app_model.client_secret,
            'grant_type': 'client_credentials'
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = self.client.post('api/v1/token', body, headers=headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_send_form(self):
        body = {
            'client_id': self.app_model.client_id,
            'client_secret': self.app_model.client_secret,
            'grant_type': 'client_credentials'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = self.client.post('api/v1/token', body, headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        payload = response.json()

        access_token = get_object(self.session.query(AccessToken).filter(
            AccessToken.access_token == payload.get('access_token')
        ))

        self.assertIsNotNone(access_token)
        self.assertEqual({'access_token': access_token.access_token, 'token_type': 'bearer'}, payload)

    def test_send_bad_grant_type(self):
        body = {
            'client_id': self.app_model.client_id,
            'client_secret': self.app_model.client_secret,
            'grant_type': 'client_credentialss'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = self.client.post('api/v1/token', body, headers=headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_send_not_exist_app(self):
        body = {
            'client_id': f'{self.app_model.client_id[:-1]}q',
            'client_secret': self.app_model.client_secret,
            'grant_type': 'client_credentials'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = self.client.post('api/v1/token', body, headers=headers)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
