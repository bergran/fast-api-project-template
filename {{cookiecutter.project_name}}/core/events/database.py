def start_database(app):

    @app.on_event('startup')
    async def wrapper():
        await start_database(app)

    return wrapper


def shutdown_database(app):

    @app.on_event('shutdown')
    async def wrapper():
        await app.database.disconnect()

    return wrapper
