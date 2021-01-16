from aiogram import Bot, types
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           InputFile, KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from settings.config import admins_id, token


bot = Bot(token=token)


async def start(message: types.Message):
    """Processing `/start` command"""
    await message.answer('Hi!')
