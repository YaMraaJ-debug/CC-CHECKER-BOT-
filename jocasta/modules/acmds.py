from datetime import datetime
from contextlib import suppress
from jocasta import bot, TICK, CROSS
from jocasta.dec import register
from jocasta.services.gate_on_off import gate_info_dec, get_status
from jocasta.services.language import change_user_lang, get_strings_dec
from jocasta.services.addtodb import user_info_callback, user_info_dec
from jocasta.services.mongo import adb
import json
from jocasta.modules.filters.user_info import get_photo_id
from jocasta.services.red import aioredis
from jocasta.utlis.send_log import send_logs
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,MessageToDeleteNotFound,InvalidQueryID)
from jocasta.services.user_allowed import only_premium


    
@register(cmds="acmds", only_admins = True, user_allowed=True)
async def acmds(message):
    try:
        await message.answer_chat_action('typing')
        text = f"""
<b>Ξ Admin Commands</b>-
<b>• Total Admin Commands: 7</b>

➥ <b>Make Premium Key</b>
⨭ Params-» days(digits)\[required] spamtime(digits and less then 30)\[optional] || test(generating 10 min key.)\[optional]
⨭ Ex-» <code>.make_key test</code>

➥ <b>Add A New Gateway</b>
⨭ Params-» cmd(string)\[required] name(string)\[required] Premium\[optional]
⨭ Ex-» <code>.add_gate chk Sirius</code>

➥ <b>Open Closed Gateway</b>
⨭ Params-» cmd(string)\[required]
⨭ Ex-» <code>.open_gate chk</code>

➥ <b>Close Opened Gateway</b>
⨭ Params-» cmd(string)\[required] reason(string)\[optional]
⨭ Ex-» <code>.close_gate chk-Error Message</code>

➥ <b>Remove Gateway</b>
⨭ Params-» cmd(string)\[required]
⨭ Ex-» <code>.rm_gate chk</code>

➥ <b>Convert Premium Gateway To Free Gateway</b>
⨭ Params-» cmd(string)\[required]
⨭ Ex-» <code>.free_gate chk</code>

➥ <b>Convert Free Gateway To Premium Gateway</b>
⨭ Params-» cmd(string)\[required]
⨭ Ex-» <code>.paid_gate chk</code>
"""
        with suppress(MessageNotModified):
            await message.reply(text)
    except Exception as e:
        await send_logs(e)
