from databases import Database

from core.utils.init_db import get_dsn


async def start_database(app):
    dsn = get_dsn(app.config)
    app_config = app.config

    database = Database(dsn)
    app_config.SQLALCHEMY_DATABASE_URI = dsn
    await database.connect()

    app.database = database
