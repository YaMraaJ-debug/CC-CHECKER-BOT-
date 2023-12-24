import json
from jocasta import bot
from jocasta.services.addtodb import user_info_dec
from jocasta.services.language import get_strings_dec
from jocasta.services.red import aioredis
from jocasta.services.mongo import adb


@user_info_dec()
@get_strings_dec('decorator_error')
async def is_user_allowed(m, user, strings):
    if user:
        return user['status'] != 'F'
    task = m.answer if hasattr(m, "message") else m.reply
    await task(strings["unknown_error"])
    return None


async def is_chat_allowed(chat_id: int) -> bool:
    return bool(await aioredis.get(f"approved_{chat_id}"))


async def get_photo_id(message) -> str:
    """Gives User Photo If user Photo is None then return jocasta photo."""

    profile_pic = await bot.get_user_profile_photos(message.from_user.id)
    if profile_pic['total_count'] == 0:
        return 'https://te.legra.ph/file/5ae0d04d2eeaa69d53cc0.jpg'
    try:
        return profile_pic['photos'][0][0]['file_id']
    except:
        return 'https://te.legra.ph/file/5ae0d04d2eeaa69d53cc0.jpg'
