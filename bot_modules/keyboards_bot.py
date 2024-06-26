from .buttons_bot import button_get_users
import aiogram

main_inline_keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard= [
        [button_get_users]
    ]
)
