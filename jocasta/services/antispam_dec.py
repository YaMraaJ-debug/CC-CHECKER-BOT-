import time

from jocasta.utlis.logger import log
from jocasta.services.red import aioredis
import os
from jocasta.services.language import get_strings
import json

async def get_spam_time(user_id: int):
    data = await aioredis.get(f"spam_{user_id}")
    if data is not None:
        data_int = int(float(data))
        return data_int
    else:
        return None


def get_spam_dec():
    def wrapped(func):
        async def wrapped_1(*args, **kwargs):
            message = args[0]
            user_info = args[2]
            res = await get_spam_time(message.from_user.id)
            if res is not None:
                strings = await get_strings(message.message.from_user.id if hasattr(message, "message") else message.from_user.id, "decorator_error")
                task = message.answer if hasattr(message, "message") else message.reply
                spam_time = int(time.time()) - int(res)
                if user_info['status'] == 'F' and spam_time < user_info['spam-time']:
                    await task(strings['antispam'].format(antispam_time= user_info['spam-time'] - spam_time))
                    return
                elif user_info['status'] == 'P' and spam_time < user_info['spam-time']:
                    await task(strings['antispam'].format(antispam_time= user_info['spam-time'] - spam_time))
                    return
                else:
                    return await func(*args, **kwargs)
            else:
                return await func(*args, **kwargs)
        return wrapped_1
    return wrapped


def pyro_spam_dec(gate_name):
    def wrapped(func):
        async def wrapped_1(*args, **kwargs):
            message = args[1]
            if (res := get_spam_time(gate_name)) is not None:
                status = res[0]
                if status == False:
                    strings = await get_strings(
                        message.message.from_user.id if hasattr(message, "message") else message.from_user.id, "decorator_error")
                    task = message.answer if hasattr(message, "message") else message.reply
                    await task(strings['gate_off'].format(gate_name=status[1],
                                                            reason=status[3],
                                                            time=status[2],
                                                            id=status[5],
                                                            name=status[4]))
                    return
                else:
                    return await func(*args, res, **kwargs)
            else:
                strings = await get_strings(message.message.from_user.id if hasattr(message, "message") else message.from_user.id,
                                            "decorator_error")
                task = message.answer if hasattr(message, "message") else message.reply
                await task(strings['gate_not_found'])
                return

        return wrapped_1

    return wrapped
