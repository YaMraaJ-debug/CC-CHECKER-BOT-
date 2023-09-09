import json
from jocasta.services.language import get_strings, get_strings_dec
from jocasta.services.red import aioredis
from jocasta.services.user_allowed import only_premium
from jocasta.utlis.helper import get_gate_info
from jocasta.utlis.logger import log
from jocasta.dec import register
from jocasta.services.addtodb import user_info_dec, user_infos
from jocasta import CROSS, TICK, bot
from jocasta.utlis.send_log import send_logs
from jocasta.services.gate_on_off import get_status
import time
from datetime import datetime
from jocasta.services.mongo import adb



@register(cmds="unban_user", only_admins=True)
@get_strings_dec("unban_user")
async def unban_user(message, lang):
    try:
        await bot.send_chat_action(chat_id = message.chat.id , action = 'typing')
        wrap = message.text.split()
        assert len(wrap) > 1, lang['error']
        if wrap[1].isdigit():
            # tool = await adb.user.update_one({'_id': })
            data = await adb.users.find_one({'_id': int(wrap[1])})
            assert data, lang['user_not_found']
            if data['warn'] > 0:
                xx = await adb.users.update_one({'_id': int(wrap[1])}, {'$set': {'warn': 0}})
                if xx: 
                    await message.reply(lang['success'].format(name = wrap[1]))
                else:
                    await message.reply(lang['error'])
            elif wrap[1].isalpha():
                data = await adb.users.find_one({'_id': wrap[1]})
            assert data, lang['user_not_found']
            if data['warn'] > 0:
                data = await adb.users.find_one({'username': wrap[1]})
                assert data, lang['user_not_found']
                xx = await adb.users.update_one({'username': wrap[1]}, {'$set': {'warn': 0}})
                if xx: 
                    await message.reply(lang['success'].format(wrap[1]))
                else:
                    await message.reply(lang['error'])
    except AssertionError as t:
        await message.reply(t)
    except Exception as e:
        await send_logs(e)