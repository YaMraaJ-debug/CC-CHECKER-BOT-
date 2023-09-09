import profile
import time
from contextlib import suppress
from jocasta import bot
from jocasta.dec import register
from jocasta.services.gate_on_off import gate_info_dec
from jocasta.services.language import get_strings_dec
from jocasta.services.addtodb import user_info_dec
from jocasta.services.mongo import adb
import json
from jocasta.modules.filters.user_info import get_photo_id
from jocasta.utlis.send_log import send_logs
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified


@register(cmds="start", user_allowed=True)
@get_strings_dec("mains")
async def start_cmd(message, lang):
    try:
        await bot.send_chat_action(chat_id = message.chat.id , action = 'typing')
        profile_pic = await get_photo_id(message)
        text = lang['start_msg'].format(
            name = message.first_name + ' '+ message.from_user.last_name if 'last_user' in  message.from_user else  message.from_user.first_name,
            id = message.from_user.id,
        )
        await message.reply_photo(profile_pic, caption = text)
    except Exception as e: 
        await send_logs(e)


# @get_strings_dec("pm_menu")
# async def get_start_func(message, strings, edit=False):
#     msg = message.message if hasattr(message, "message") else message

#     task = msg.edit_text if edit else msg.reply
#     buttons = InlineKeyboardMarkup()
#     buttons.add(InlineKeyboardButton(strings["btn_help"], callback_data="get_help"))
#     buttons.add(
#         InlineKeyboardButton(strings["btn_lang"], callback_data="lang_btn"),
#         InlineKeyboardButton(
#             strings["btn_source"], url="https://github.com/TeamDaisyX/"
#         ),
#     )
#     buttons.add(
#         InlineKeyboardButton(strings["btn_channel"], url="https://t.me/DaisyXUpdates"),
#         InlineKeyboardButton(
#             strings["btn_group"], url="https://t.me/DaisySupport_Official"
#         ),
#     )
#     buttons.add(
#         InlineKeyboardButton(
#             "👸🏼 Add DaisyX to your group",
#             url=f"https://telegram.me/daisyxbot?startgroup=true",
#         )
#     )
#     # Handle error when user click the button 2 or more times simultaneously
#     with suppress(MessageNotModified):
#         await task(strings["start_hi"], reply_markup=buttons)

# @register(f = "text")
# @get_strings_dec("mains")
# @user_info_dec()
# # @gate_info_dec("ch")
# async def test(message, lang, user):
#     if user['status'] == 'P' and  int(time.time()) > user['expiry']:
#         await adb.users.update_one({'_id': message.from_user.id}, {'$set': {'status': "F", 'role': "Free"}})
#         task = message.answer if hasattr(message, "message") else message.reply
#         await task(lang['premium_expired'])

