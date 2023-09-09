import profile
import time

from jocasta.services.red import  aioredis
from jocasta import bot
from jocasta.dec import register
from jocasta.services.language import get_strings_dec
from jocasta.services.addtodb import user_info_dec
import json
from jocasta.modules.filters.user_info import get_photo_id
import time
from jocasta.utlis.send_log import send_logs

# @register(f = "text", is_warned = True)
# @user_info_dec()
# async def check_user(message, user):
#     pass



@register(cmds="addgp", user_allowed = True, only_admins = True)
async def add_groups(message):
    try:
        await bot.send_chat_action(chat_id = message.chat.id , action = 'typing')
        if await aioredis.get(f"approved_{str(message.chat.id)}"):
            await message.reply(f"<code>{message.chat.id}</code> Is Already Added.")
        else:
            await aioredis.set(f"approved_{str(message.chat.id)}", "True")
            await message.reply(f"Added <code>{message.chat.id}</code>.")
    except Exception as e: 
        await send_logs(e)


@register(cmds="rmgp", user_allowed = True, only_admins = True)
async def remove_groups(message):
    try:
        await bot.send_chat_action(chat_id = message.chat.id , action = 'typing')
        if not await aioredis.get(f"approved_{str(message.chat.id)}"):
            await message.reply(f"<code>{message.chat.id}</code> Is Already Removed.")
        else:
            await aioredis.delete(f"approved_{str(message.chat.id)}")
            await message.reply(f"Removed <code>{message.chat.id}</code>.")
    except Exception as e: 
        await send_logs(e)

# @register(f = "any")
# async def test(message):
#     print(message)
