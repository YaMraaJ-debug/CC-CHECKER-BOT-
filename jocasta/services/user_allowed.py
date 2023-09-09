import json
from jocasta.modules.filters.user_info import is_chat_allowed
from jocasta.services.gate_on_off import get_status
from jocasta.utlis.logger import log
from jocasta.services.red import aioredis
from jocasta.services.mongo import adb
import os
import time
from babel.core import Locale
from jocasta.services.language import get_strings
from contextlib import suppress
from jocasta.modules.filters.user_info import is_chat_allowed
from jocasta.services.addtodb import user_infos
from jocasta.utlis.logger import log
from jocasta.services.red import aioredis
import os
from jocasta.services.mongo import adb
from jocasta.services.language import get_strings
import json
from aiogram.utils.exceptions import MessageCantBeEdited, MessageToEditNotFound



async def user_infos_allowed(message):
    user_info = await user_infos(message)
    strings = await get_strings(message.message.from_user.id if hasattr(message, "message") else message.from_user.id,"decorator_error")
    task = message.answer if hasattr(message, "message") else message.reply
    data = False if user_info['status'] == 'F' else True
    if not data and message.chat.type == 'private':
        await task(strings["no_access"])
        return False
    elif not data and message.chat.type != 'private':
        if await is_chat_allowed(message.chat.id):
            return True
        else:
            await task(strings["no_groups"])
            return False
    else:
        return True






# async def check(message,user_info) -> bool:
    
#     if user_info:
#         if user_info['status'] == 'F':
#             return False
#         else:
#             return True
#     else:
#         task = message.answer if hasattr(message, "message") else message.reply
#         await task(strings["unknown_error"])
#         return None



def only_premium():
    def wrapped(func):
        async def wrapped_1(*args, **kwargs):
            message = args[0]
            x = await user_infos_allowed(message)
            if x:
                with suppress(MessageCantBeEdited, MessageToEditNotFound):
                    return await func(*args, **kwargs)
            else:
                return

        return wrapped_1

    return wrapped