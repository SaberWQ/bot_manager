from .keyboards_bot import main_inline_keyboard
from aiogram.filters import CommandStart
from aiogram.types import Message
from .dispatcher_bot import dispatcher
from .loader import loader_file
from .text import text
from .create_bot import bot

@dispatcher.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(text = 'Hello', reply_markup= main_inline_keyboard)
    # for mes in message:
        # print(mes)
    # await message.answer_photo(photo = loader_file(file_name= "orig.png"), caption= text)