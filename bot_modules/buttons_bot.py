import aiogram 

button_get_users = aiogram.types.InlineKeyboardButton(text = "GET USERS", callback_data = "users")

button_del_users = aiogram.types.InlineKeyboardButton(text = "DEL USER", callback_data = "del")
button_admin_users = aiogram.types.InlineKeyboardButton(text = "IS ADMIN", callback_data = "is_admin")