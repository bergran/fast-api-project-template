# -*- coding: utf-8 -*-
from starlette import status

from core.test.transaction_test_case import TransactionTestCase


class HealthCheckTestCase(TransactionTestCase):

    def test_health_check(self):
        response = self.client.get('/api/v1/health-check')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
