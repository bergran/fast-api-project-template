from unittest import TestCase

import pytest


@pytest.mark.usefixtures("get_session_and_client_fixture")
class TransactionTestCase(TestCase):

    def tearDown(self):
        meta = self.Base.metadata
        for table in reversed(meta.sorted_tables):
            self.session.execute(table.delete())
        self.session.commit()
