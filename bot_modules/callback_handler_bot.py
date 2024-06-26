from aiogram.types import CallbackQuery
from .dispatcher_bot import dispatcher
import sqlite3
from .buttons_bot import button_del_users, button_admin_users
from .keyboards_bot import main_inline_keyboard
from .create_bot import bot

@dispatcher.callback_query()
async def callback_handler(callback: CallbackQuery):

    data_base = sqlite3.connect('flask_cart/instance/data.db')
    cursor = data_base.cursor()

    if callback.data == "users":
        
        main_inline_keyboard.inline_keyboard[0] = [button_admin_users, button_del_users]

        cursor.execute("SELECT * FROM user")
    
        list_users = cursor.fetchall()
        for user in list_users:
            # user = [1, 'Nick', "0000", 1]
            button_del_users.callback_data = f'del-{user[0]}' # 'del-1 or del-2 or del-10

            if int(user[3]) == 1:
                button_admin_users.callback_data = f"disable_admin-{user[0]}"
                button_admin_users.text = "DISABLE ADMIN"
            else:
                button_admin_users.callback_data = f"is_admin-{user[0]}"
                button_admin_users.text = "IS ADMIN"

            await bot.send_message(
                chat_id= callback.message.chat.id, 
                text= f"🆔: {user[0]}\n👤: {user[1]}\n🔒: {user[2]}\nis_admin: {user[3]}", 
                message_thread_id= 2,
                reply_markup= main_inline_keyboard
            )
    elif "del" in callback.data:
        button_data = callback.data.split('-') # button_data = ['del', '1']
        user_id = int(button_data[-1]) # user_id = 1

        button_admin_users.callback_data = f"yes-{user_id}"
        button_admin_users.text = "YES"

        button_del_users.callback_data = f"no-{user_id}"
        button_del_users.text = "NO"

        main_inline_keyboard.inline_keyboard[0] = [button_admin_users, button_del_users]
        await callback.message.edit_reply_markup(inline_message_id= callback.inline_message_id, reply_markup= main_inline_keyboard)

    elif "no" in callback.data:
        button_data = callback.data.split("-")
        user_id = int(button_data[-1])
        cursor.execute("SELECT * FROM user WHERE id = ?", [user_id])
        user = cursor.fetchall()[0]
        
        if user[3] == 0:
            button_admin_users.callback_data = f"is_admin-{user_id}"
            button_admin_users.text = "IS ADMIN"
        else:
            button_admin_users.callback_data = f"disable_admin-{user_id}"
            button_admin_users.text = "DISABLE ADMIN"
        button_del_users.callback_data = f'del-{user_id}'
        button_del_users.text = "DEL USER"
        main_inline_keyboard.inline_keyboard[0] = [button_admin_users, button_del_users]
        await callback.message.edit_reply_markup(inline_message_id= callback.inline_message_id, reply_markup= main_inline_keyboard)
    #
    elif "yes" in callback.data:
        button_data = callback.data.split("-")
        user_id = int(button_data[-1])

        cursor.execute("DELETE FROM user WHERE id = ?", [user_id])
        await callback.message.delete()
        button_del_users.text = "DEL USER"
        button_admin_users.callback_data = f"del-{user_id}"
    #   
    elif "disable_admin" in callback.data:
        button_data = callback.data.split("-")
        user_id = int(button_data[-1])
        cursor.execute("UPDATE user SET is_admin = ? WHERE id = ?", [0, user_id])

        button_admin_users.callback_data = f"is_admin-{user_id}"
        button_admin_users.text = "IS ADMIN"

        cursor.execute("SELECT * FROM user WHERE id = ?", [user_id])
        user = cursor.fetchone()

        await callback.message.edit_text(
            text = f"🆔: {user[0]}\n👤: {user[1]}\n🔒: {user[2]}\n➡️is_admin: {user[3]}❌",
            reply_markup= main_inline_keyboard
        )
    #
    elif "is_admin" in callback.data:
        button_data = callback.data.split("-")
        user_id = int(button_data[-1])

        cursor.execute("UPDATE user SET is_admin = ? WHERE id = ?", [1, user_id])

        button_admin_users.callback_data = f"disable_admin-{user_id}"
        button_admin_users.text = "DISABLE ADMIN"

        cursor.execute("SELECT * FROM user WHERE id = ?", [user_id])
        user = cursor.fetchone()

        await callback.message.edit_text(
            text = f"🆔: {user[0]}\n👤: {user[1]}\n🔒: {user[2]}\n➡️is_admin: {user[3]}✅",
            reply_markup= main_inline_keyboard
        )
    
    
    data_base.commit()
    data_base.close()
# 
# 
# 

