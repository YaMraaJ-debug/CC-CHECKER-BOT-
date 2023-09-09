import json
from jocasta.services.language import get_strings, get_strings_dec
from jocasta.services.red import aioredis
from jocasta.utlis.helper import get_gate_info
from jocasta.utlis.logger import log
from jocasta.dec import register
from jocasta.services.addtodb import user_info_dec
from jocasta import CROSS, TICK, bot
from jocasta.utlis.send_log import send_logs
from jocasta.services.gate_on_off import get_status
import time
from datetime import datetime




@register(cmds="add_gate", user_allowed=True, only_admins=True)
@get_strings_dec("add_gate")
async def add_gate(message, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        msg = await message.reply(lang['start_msg'])
        data = message.text.split(' ')
        assert len(data) > 1 and not data[1].isdigit() and data[2], lang['error']
        if await get_status(data[1].lower()):
            await msg.edit_text(lang['already_found'])
        else:
            is_premium = False if len(data) == 3 else True
            data_to_post = {
"status": "✅",
"name": data[2].title(),
"premium": is_premium,
"user_id": message.from_user.id,
"is_closed": False,
"date": datetime.today().strftime('%Y-%m-%d'),
            }
            data_to_post_str = json.dumps(data_to_post)  
            res = await aioredis.set(f"gate_{data[1].lower()}", data_to_post_str)
            if res:
                await msg.edit_text(lang['success'])
            else:
                await msg.edit_text(lang['already_found'])
    except AssertionError as err:
        await msg.edit_text(err)
    except Exception as ex:
        await send_logs(ex)


@register(cmds="open_gate", user_allowed=True, only_admins=True)
@get_strings_dec("open_gate")
async def add_gate(message, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        msg = await message.reply(lang['start_msg'])
        data = message.text.split(' ')
        assert len(data) == 2 and data[1].isalpha(), lang['error']
        dat = await get_gate_info(data[1].lower())
        if not dat:
            await msg.edit_text(lang['already_opened'])
        else:
            dat1 = dat
            dat1['is_closed'] = False
            dat1['date'] = datetime.today().strftime('%Y-%m-%d')
            dat1["user_id"] = message.from_user.id
            dat1['status'] = TICK
            dat1.pop('reason')
            up_data = json.dumps(dat1)
            res = await aioredis.set(f"gate_{data[1].lower()}", up_data)
            if res:
                await msg.edit_text(lang['success'])
            else:
                await msg.edit_text(lang['already_opened'])
    except AssertionError as err:
        await msg.edit_text(err)
    except Exception as ex:
        await send_logs(ex)


@register(cmds="rm_gate", user_allowed=True, only_admins=True)
@get_strings_dec("rm_gate")
async def rm_gate(message, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        msg = await message.reply(lang['start_msg'])
        data = message.text.split(' ')
        assert len(data) == 2 and data[1].isalpha(), lang['error']
        if await get_gate_info(data[1]):
            res = await aioredis.delete(f"gate_{data[1].lower()}")
            if res:
                await msg.edit_text(lang['success'])
            else:
                await msg.edit_text(lang['already_removed'])
        else:
            await msg.edit_text(lang['gate_not_found'])
    except AssertionError as err:
        await msg.edit_text(err)
    except Exception as ex:
        await send_logs(ex)


@register(cmds="close_gate", user_allowed=True, only_admins=True)
@get_strings_dec("close_gate")
async def close_gate(message, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        msg = await message.reply(lang['start_msg'])
        data1 = message.text.split('-')
        data = data1[0].split(' ')
        assert len(data) == 2, lang['error']
        dat = await get_gate_info(data[1])
        if not dat :
                await msg.edit_text(lang['gate_not_found'])
        elif dat['is_closed']:
            await msg.edit_text(lang['already_closed'])
        else:
            dat1 = dat
            dat1['is_closed'] = True
            dat1['date'] = datetime.today().strftime('%Y-%m-%d')
            dat1["user_id"] = message.from_user.id
            dat1['status'] = '❌'
            dat1['reason'] = data1[1]
            check = await aioredis.set(f"gate_{data[1].lower()}", json.dumps(dat1))
            if check:
                await msg.edit_text(lang['success'])
            else:
                await msg.edit_text(lang['gate_not_found'])
    except AssertionError as err:
        await msg.edit_text(err)
    except Exception as ex:
        await send_logs(ex)






@register(cmds="free_gate", user_allowed=True, only_admins=True)
@get_strings_dec("free_gate")
async def free_gate(message, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        msg = await message.reply(lang['start_msg'])
        data = message.text.split(' ')
        assert len(data) == 2 and data[1].isalpha(), lang['error']
        dat = await get_gate_info(data[1])
        if dat and not dat['premium']:
            await msg.edit_text(lang['already_free'])
        else:
            if not dat :
                await msg.edit_text(lang['gate_not_found'])
            else:
                dat1 = dat
                dat1['premium'] = False
                dat1['date'] = datetime.today().strftime('%Y-%m-%d')
                dat1["user_id"] = message.from_user.id
                check = await aioredis.set(f"gate_{data[1].lower()}", json.dumps(dat1))
                if check:
                    await msg.edit_text(lang['success'])
                else:
                    await msg.edit_text(lang['gate_not_found'])
    except AssertionError as err:
        await msg.edit_text(err)
    except Exception as ex:
        await send_logs(ex)





@register(cmds="paid_gate", user_allowed=True, only_admins=True)
@get_strings_dec("paid_gate")
async def paid_gate(message, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        msg = await message.reply(lang['start_msg'])
        data = message.text.split(' ')
        assert len(data) == 2 and data[1].isalpha(), lang['error']
        dat = await get_gate_info(data[1])
        if dat and dat['premium']:
            await msg.edit_text(lang['already_free'])
        else:
            if not dat:
                await msg.edit_text(lang['gate_not_found'])
            else:
                dat1 = dat
                dat1['premium'] = True
                dat1['date'] = datetime.today().strftime('%Y-%m-%d')
                dat1["user_id"] = message.from_user.id
                check = await aioredis.set(f"gate_{data[1].lower()}", json.dumps(dat1))
                if check:
                    await msg.edit_text(lang['success'])
                else:
                    await msg.edit_text(lang['gate_not_found'])
    except AssertionError as err:
        await msg.edit_text(err)
    except Exception as ex:
        await send_logs(ex)
