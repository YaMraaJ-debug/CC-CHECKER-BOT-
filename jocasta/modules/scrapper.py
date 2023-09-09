import os
from asyncio import sleep
from jocasta.services.userbot import ubot
from jocasta import bot
from jocasta.dec import register
from jocasta.services.language import get_strings_dec
from jocasta.services.addtodb import user_info_dec
from jocasta.services.pyro import pbot
from jocasta.utlis.send_log import send_logs
import re
from os.path import exists


@register(cmds="scrapper", only_admins=True)
@get_strings_dec("scrapper")
@user_info_dec()
async def scrapper(message, lang, user):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        msg = await message.reply(lang['start_msg'])
        input_data = message.text.split(' ')
        assert len(input_data) == 3, lang['error']
        assert input_data[1].isalnum(), lang['error']
        assert input_data[2].isdigit(), lang['error']
        a = await ubot.get_messages(input_data[1], limit=int(input_data[2]))
        assert a, lang['not_found']
        length = 0
        await msg.edit_text(lang['half'].format(amount=len(a)))
        file = open(f'scrapped_{input_data[1]}.txt', "a")
        for x in a:
            if not hasattr(x, 'message'): continue
            if not isinstance(x.message, str): continue
            if len(x.message) == 0: continue
            if len(x.message) < 28: continue
            res = re.findall(r'\d+', x.message)
            if len(res) < 3: continue
            if len(res[0]) not in [15, 16]: continue
            cc = str(res[0])
            mes = str(res[1])
            ano = str(res[2])
            cvv = str(res[3])
            if len(res[1]) == 3:
                cvv = str(res[1])
                mes = str(res[2])
                ano = str(res[3])
            data_save = str(cc + "|" + mes + "|" + ano + "|" + cvv + '\n')
            file.write(data_save)
            length += 1
        if length > 0:
            await msg.edit_text(lang['success'])
            found = f"""
Found {length} Cards in @{input_data[1]}
"""
            file.close()
            sleep(3)
            await pbot.send_document(chat_id=message.chat.id, document=f'scrapped_{input_data[1]}.txt',
                                    caption=found)  # await message.reply(dict(x.message))
            os.remove(f'scrapped_{input_data[1]}.txt')
        else:
            await msg.edit_text(lang['no_cards'])
    except AssertionError as t:
        await msg.edit_text(t)
    except Exception as e:
        await msg.edit_text(lang['error'])
        await send_logs(e)
