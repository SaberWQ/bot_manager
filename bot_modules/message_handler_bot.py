import os
from .create_bot import bot
from .dispatcher_bot import dispatcher
from aiogram.types import Message

@dispatcher.message()

async def message_handler(message: Message):
    abs_path_images = os.path.abspath(__file__ + f"/../../images")
    if message.photo:
        print(message.photo[-1])
        file_id = message.photo[-1].file_id
        photo = await bot.get_file(file_id= file_id)
        photo_path = photo.file_path
        photo_name = photo.file_unique_id
        await bot.download_file(file_path= photo_path, destination= f"{abs_path_images}/{photo_name}.png")
        

