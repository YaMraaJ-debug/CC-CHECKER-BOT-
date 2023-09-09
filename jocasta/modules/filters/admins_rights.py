import pickle
import re
from contextlib import suppress
from typing import Union

from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import BadRequest, ChatNotFound, Unauthorized
from telethon.tl.functions.users import GetFullUserRequest
from jocasta import ADMINS, bot
# from jocasta.services.mongo import db
from jocasta.services.red import aioredis
# from jocasta.services.tele import tbot

# from jocasta.services.language import get_strings





async def check_admin_rights(
    event: Union[Message, CallbackQuery], chat_id, user_id, rights
):
    # User's pm should have admin rights
    if chat_id == user_id:
        return True

    if user_id in ADMINS:
        return True

    # Workaround to support anonymous admins
    if user_id == 1087968824:
        if not isinstance(event, Message):
            raise ValueError(
                f"Cannot extract signuature of anonymous admin from {type(event)}"
            )

        if not event.author_signature:
            return True

        for admin in (await get_admins_rights(chat_id)).values():
            if "title" in admin and admin["title"] == event.author_signature:
                for permission in rights:
                    if not admin[permission]:
                        return permission
        return True

    admin_rights = await get_admins_rights(chat_id)
    if user_id not in admin_rights:
        return False

    if admin_rights[user_id]["status"] == "creator":
        return True

    for permission in rights:
        if not admin_rights[user_id][permission]:
            return permission

    return True



async def get_admins_rights(chat_id, force_update=False):
    key = "admin_cache:" + str(chat_id)
    if (alist := await aioredis.get(key)) and not force_update:
        return pickle.loads(alist)
    else:
        alist = {}
        admins = await bot.get_chat_administrators(chat_id)
        for admin in admins:
            user_id = admin["user"]["id"]
            alist[user_id] = {
                "status": admin["status"],
                "admin": True,
                "title": admin["custom_title"],
                "anonymous": admin["is_anonymous"],
                "can_change_info": admin["can_change_info"],
                "can_delete_messages": admin["can_delete_messages"],
                "can_invite_users": admin["can_invite_users"],
                "can_restrict_members": admin["can_restrict_members"],
                "can_pin_messages": admin["can_pin_messages"],
                "can_promote_members": admin["can_promote_members"],
            }

            with suppress(KeyError):  # Optional permissions
                alist[user_id]["can_post_messages"] = admin["can_post_messages"]

        await aioredis.set(key, pickle.dumps(alist))
        await aioredis.expire(key, 900)
    return alist




async def is_user_admin(chat_id, user_id):
    # User's pm should have admin rights
    if chat_id == user_id:
        return True

    if user_id in ADMINS:
        return True

    try:
        admins = await get_admins_rights(chat_id)
    except:
        return False
    else:
        if user_id in admins:
            return True
        else:
            return False
