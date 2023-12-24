import json
from jocasta.utlis.logger import log
from jocasta.services.red import aioredis
from jocasta.services.mongo import adb
import os
import time
from jocasta.services.language import get_strings

db = adb.chat_settings


async def get_chat_info(chat_id: int):
    return data if (data := await db.find_one({'_id': chat_id})) else None


async def set_chat_info(data: dict, chat_id: int):
    if (data := await db.insert_one(data)):
        return data
    else:
        return await get_chat_info(chat_id)


async def chat_info(message):
    data = message.message if hasattr(message, "message") else message
    user_id = data.chat.id
    data = {
        '_id': user_id,
    }
    if (res := await get_chat_info(user_id)) is None:
        if (check := await set_chat_info(data, user_id)) is None:
            strings = await get_strings(message.message.from_user.id if hasattr(message, "message") else message.from_user.id,
                                        "decorator_error")
            task = message.answer if hasattr(message, "message") else message.reply
            await task(strings['no_register'])
        else:
            res = check
    else:
        res = res



    class Strings:
        @staticmethod
        def chat_info(name, res):
            return res if name in res else {}

        def user_info(self, name):
            data = self.chat_info(name, res)
            return {} if name not in data else data

        def __getitem__(self, key):
            return self.user_info(key)


    return Strings()


def get_chat_dec():
    def wrapped(func):
        async def wrapped_1(*args, **kwargs):
            message = args[0]
            x = await chat_info(message)
            return await func(*args, x, **kwargs)

        return wrapped_1

    return wrapped

