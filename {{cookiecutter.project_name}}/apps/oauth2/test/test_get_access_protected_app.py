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

        self.access_token_good = AccessToken(scopes=['me'])
        self.access_token_bad = AccessToken(scopes=['em'])
        self.access_token_superset = AccessToken(scopes=['me', 'em'])
        self.access_token_none = AccessToken(scopes=[])

        self.app_model.access_tokens.append(self.access_token_bad)
        self.app_model.access_tokens.append(self.access_token_good)
        self.app_model.access_tokens.append(self.access_token_superset)
        self.app_model.access_tokens.append(self.access_token_none)
        session.commit()

    def test_get_app_good_scopes(self):
        headers = {
            'Authorization': f'bearer {self.access_token_good.access_token}'
        }

        response = self.client.get('api/v1/me', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        payload = response.json()

        self.assertIn('name', payload)
        self.assertIn('created', payload)
        self.assertIn('modified', payload)

    def test_get_app_good_scopes_superset(self):
        headers = {
            'Authorization': f'bearer {self.access_token_superset.access_token}'
        }

        response = self.client.get('api/v1/me', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        payload = response.json()

        self.assertIn('name', payload)
        self.assertIn('created', payload)
        self.assertIn('modified', payload)

    def test_get_app_good_scopes_none(self):
        headers = {
            'Authorization': f'bearer {self.access_token_none.access_token}'
        }

        response = self.client.get('api/v1/me', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_app_bad_scopes(self):
        headers = {
            'Authorization': f'bearer {self.access_token_bad.access_token}'
        }

        response = self.client.get('api/v1/me', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_app_bad_auth(self):
        headers = {
            'Authorization': f'bearer fff'
        }

        response = self.client.get('api/v1/me', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
