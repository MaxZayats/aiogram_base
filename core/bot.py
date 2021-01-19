import logging

from aiogram import Bot, Dispatcher, executor, types
from settings.config import admins_id, token
from core.handlers import set_handlers


logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)

dp = Dispatcher(bot)
set_handlers(dp)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.callback_query_handler()
async def process_callback_buttons(callback_query: types.CallbackQuery):
    # do something
    await callback_query.answer()


@dp.message_handler(content_types=['photo', 'video', 'document'])
async def receive_media(message: types.Message):
    # do something
    pass    


def start():
    from core.events import on_shutdown, on_startup
    executor.start_polling(dispatcher=dp, on_startup=on_startup, on_shutdown=on_shutdown)
