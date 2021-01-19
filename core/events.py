async def on_startup(dispatcher):
    from core.db_wrapper import database
    if not database.is_connected:
        await database.connect()


async def on_shutdown(dispatcher):
    from core.db_wrapper import database
    if database.is_connected:
        await database.disconnect()
