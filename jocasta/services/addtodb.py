from datetime import datetime
import json
from jocasta.utlis.logger import log
from jocasta.services.red import aioredis
from jocasta.services.mongo import adb
import os
import time
from babel.core import Locale
from jocasta.services.language import get_strings


async def get_user_info(chat_id: int):
    if (data := await adb.users.find_one({'_id': chat_id})):
        return data
    else:
        return None


async def set_user_info(data: dict, chat_id: int):
    x = await adb.users.insert_one(data)
    if x:
        return await get_user_info(chat_id)
    else: return None


async def user_infos(message):
    
    data = message.message if hasattr(message, "message") else message
    user_id = data.from_user.id 
    if (res := await get_user_info(user_id)) is None:
        data = {
        '_id': user_id,
        'username': data.from_user.username,
        'reg-date': datetime.today().strftime('%Y-%m-%d'),
        'status': 'F',
        'spam-time': 60,
        'antispam': True,
        'save-ccs': True,
        'role': 'Free',
        'warn': 0,
        
    }
        if (check := await set_user_info(data, user_id)) is None:
            strings = await get_strings(message.message.from_user.id if hasattr(message, "message") else message.from_user.id,"decorator_error")
            task = message.answer if hasattr(message, "message") else message.reply
            await task(strings['no_register'])
        else:
            res = check
    else:
        res = res
    task = message.answer if hasattr(message, "message") else message.reply
    strings = await get_strings(message.message.from_user.id if hasattr(message, "message") else message.from_user.id,"decorator_error")
    if res['warn'] > 5:
        task = message.message.reply if hasattr(message, "message") else message.reply
        await task(strings["warned"])
        return False
    if res['status'] == 'P' and  int(time.time()) > res['expiry']:
        await adb.users.update_one({'_id':message.message.from_user.id if hasattr(message, "message") else message.from_user.id}, {'$set': {'status': "F", 'role': "Free"}})
        await task(strings['premium_expired'])
        return False
    return None if not res else res
    # class Strings:
    #     @staticmethod
    #     def user_infos(name, res):
    #         if name in res:
    #             return res
    #         else:
    #             return {}

    #     def user_info(self, name):
    #         data = self.user_infos(name, res)
    #         if name not in data:
    #             return None
    #         return data[name]

    #     def __getitem__(self, key):
    #         return self.user_info(key)

    # return Strings()


def user_info_dec():
    def wrapped(func):
        async def wrapped_1(*args, **kwargs):
            message = args[0]
            x = await user_infos(message)
            if x:
                return await func(*args, x, **kwargs)
        return wrapped_1
    return wrapped

def user_info_callback():
    def wrapped(func):
        async def wrapped_1(*args, **kwargs):
            message = args[0]
            x = await user_infos(message.message)
            if x:
                return await func(*args, x, **kwargs)
        return wrapped_1
    return wrapped


def pyro_user_info_dec():
    def wrapped(func):
        async def wrapped_1(*args, **kwargs):
            message = args[1]
            x = await user_infos(message)
            if x:
                return await func(*args, x, **kwargs)
        return wrapped_1
    return wrapped
