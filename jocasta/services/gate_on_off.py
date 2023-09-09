from contextlib import suppress
import time
from jocasta.modules.filters.user_info import is_chat_allowed
from jocasta.services.addtodb import user_infos
from jocasta.utlis.logger import log
from jocasta.services.red import aioredis
import os
from jocasta.services.mongo import adb
from jocasta.services.language import get_strings
import json
from aiogram.utils.exceptions import MessageCantBeEdited, MessageToEditNotFound

async def get_status(gate_name: str):
    data = await aioredis.get(f"gate_{gate_name.lower()}")
    if data:
        return json.loads(data)
    else:
        return False


def gate_info_dec(gate_name):
    def wrapped(func):
        async def wrapped_1(*args, **kwargs):
            start_time = time.time()
            message = args[0]
            user_info = await user_infos(message)
            strings = await get_strings(message.message.from_user.id if hasattr(message, "message") else message.from_user.id,"decorator_error")
            task = message.answer if hasattr(message, "message") else message.reply
            if res := await get_status(gate_name):
                if res['is_closed']:
                    mess = strings['gate_off'].format(gate_name=str(res['name']),reason=res['reason'] if 'reason' in res else "Unknown Error.",time=res['date'], name = res['user_id'], id = res['user_id'])
                    await task(mess, parse_mode = 'html')
                    return
                else:
                    data = False if user_info['status'] == 'F' else True
                    if data and res['premium']:
                        with suppress(MessageCantBeEdited, MessageToEditNotFound):
                            return await func(*args, res,user_info, start_time, **kwargs)
                    elif not data and res['premium']:
                        await task(strings["only_premium"])
                        return False
                    elif not data and message.chat.type == 'private':
                        await task(strings["no_access"])
                        return False
                    elif not data and message.chat.type != 'private':
                        if await is_chat_allowed(message.chat.id):
                            with suppress(MessageCantBeEdited, MessageToEditNotFound):
                                return await func(*args, res,user_info, start_time, **kwargs)
                        else:
                            await task(strings["no_groups"])
                            return False
                    else:
                        with suppress(MessageCantBeEdited, MessageToEditNotFound):
                                return await func(*args, res,user_info, start_time, **kwargs)
            else:
                with suppress(MessageCantBeEdited, MessageToEditNotFound):
                    await task(strings['gate_not_found'])
                    return 
        return wrapped_1
    return wrapped
