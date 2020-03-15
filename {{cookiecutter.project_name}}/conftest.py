import asyncio
import logging
import os

import pytest
from sqlalchemy_utils import database_exists, drop_database, create_database
from starlette.testclient import TestClient

from core.db.start_database import start_database
from core.utils.init_db import get_dsn

logger = logging.getLogger('fixture')
logger.setLevel(logging.INFO)


pytestmark = pytest.mark.asyncio


def pytest_sessionstart(session):
    os.environ.setdefault('TEST_RUN', '1')
    from main import app
    _create_database(get_dsn(app.config))
    _create_database_connection(app)


def pytest_sessionfinish(session):
    os.environ.setdefault('TEST_RUN', '1')
    from main import app
    _delete_database(get_dsn(app.config))


def _create_database(dsn):
    database_name = dsn.split('/')[-1]
    logger.info('check database {}'.format(database_name))

    db_exists = database_exists(dsn)
    if db_exists:
        logger.warning('drop old database {}'.format(database_name))
        drop_database(dsn)

    logger.info('create new database {}'.format(database_name))
    create_database(dsn)


@pytest.yield_fixture(scope='class')
def event_loop(request):
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="class")
async def get_session_and_client_fixture(request):
    from main import app
    # Set TEST_RUN environment to tell app that we are running under test environment to connect dummy test
    os.environ.setdefault('TEST_RUN', '1')

    from core.db.base import Base

    await start_database(app)
    request.cls.client = TestClient(app)
    request.cls.Base = Base
    request.cls.database = app.database


def _delete_database(dsn):
    database_name = dsn.split('/')[-1]
    logger.info('drop old database {}'.format(database_name))
    drop_database(dsn)


def _create_database_connection(app):
    start_database(app)

    import subprocess
    subprocess.call("cd {} && sh scripts/migrate.sh head".format(app.config.BASE_DIR), shell=True)
