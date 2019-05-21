# -*- coding: utf-8 -*-


def get_dsn(config):
    assert config is not None, 'Need to inject ConfigMiddleware'

    databases = config._DATABASES.copy()
    database_user = config.DATABASES.copy()

    if config.TEST_RUN:
        database_user.update(config.TEST)

    for key, value in database_user.items():
        if value:
            databases[key] = value

    SQLALCHEMY_DATABASE_URI = '{type}://{username}:{password}@{host}:{port}/{database}'.format(
        **databases
    )

    return SQLALCHEMY_DATABASE_URI
