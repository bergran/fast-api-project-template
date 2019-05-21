# -*- coding: utf-8 -*-
from starlette import status

from core.test.transaction_test_case import TransactionTestCase


class HelloWorldTestCase(TransactionTestCase):

    def test_get_response(self):
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Hello World"})