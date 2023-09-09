from contextlib import suppress
from jocasta import bot, TICK, CROSS
from jocasta.dec import register
from jocasta.services.gate_on_off import get_status
from jocasta.services.language import change_user_lang, get_strings_dec
from jocasta.services.addtodb import user_info_callback
from jocasta.services.mongo import adb
from jocasta.services.red import aioredis
from jocasta.utlis.send_log import send_logs
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.exceptions import MessageNotModified, MessageToDeleteNotFound
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,MessageToDeleteNotFound,InvalidQueryID)


@register(cmds="cmds", user_allowed=True)
@get_strings_dec("cmds")
async def start_cmd(message, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        markup = await get_cmds_func(message)
        le = await aioredis.keys('gate_*')
        with suppress(MessageNotModified, MessageToDeleteNotFound):
            await message.reply(lang['start_msg'].format(name=message.from_user.first_name, id=message.from_user.id, total = len(le)),reply_markup=markup)
    except Exception as e:
        await send_logs(e)

@register(cmds="buy", user_allowed=True)
@get_strings_dec("buy")
async def start_cmd(message, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        buttons = InlineKeyboardMarkup()
        buttons.add(
        InlineKeyboardButton('Click To Buy', url='https://t.me/r0ld3x'),
        InlineKeyboardButton('Support Channel', url='https://t.me/roldexverse')
    )
        text = """
<b>≛ Premium Plans</b>:-
<b>5$-» 20 Days</b>
<b>10$-» 50 Days</b>
<b>20$-» 120 Days</b>
<b>25$-» 150 Days</b>

Dm </code>@r0ld3x</code> If Intrested.

<b>Payment Methods</b>-» <b>Airtm, CryptoCurrency, Upi, etc.</b>
"""
        await message.reply_text(text=text)
        with suppress(MessageNotModified, MessageToDeleteNotFound):
            await message.reply(text,reply_markup=buttons)
    except Exception as e:
        await send_logs(e)


@get_strings_dec("cmds_vars")
async def get_cmds_func(message, strings):
    buttons = InlineKeyboardMarkup()
    buttons.add(
        InlineKeyboardButton(strings["auth"], callback_data="auth"),
        InlineKeyboardButton(strings["charge"], callback_data="charge")
    )
    buttons.add(
        InlineKeyboardButton(strings["others"], callback_data="others"),
        InlineKeyboardButton(strings["settings"], callback_data="settings")
    )
    buttons.add(
        InlineKeyboardButton(strings["close"], callback_data="close"),
        # InlineKeyboardButton(
        #     strings["btn_group"], url="https://t.me/DaisySupport_Official"
        # ),
    )
    return buttons


##AUTH###

@register(regexp="auth", user_callback=True, f="cb")
@get_strings_dec("cmds_vars")
async def auth(event,lang):
    chk = await get_status('chk')
    mess_chk = f'⨭ Reason-» {chk["reason"]} \n' if 'reason' in chk else '⨭ Ex-»<code>/chk cc|mm|yy|cvv</code>\n'
    zho = await get_status('zho')
    mess_zho = f'⨭ Reason-» {zho["reason"]} \n' if 'reason' in zho else '⨭ Ex-»<code>/zho cc|mm|yy|cvv</code>\n'
    text = f"""
<b>Ξ Charge gates</b>-
<b>• Total Charge Gates: 8</b>

➥ <b>{chk['name']}</b>-» {chk['status']} || {chk['date']}
⨭ Only For Premium Users-» {chk['premium']} 
{mess_chk}
➥ <b>{zho['name']}</b>-» {zho['status']} || {zho['date']}
⨭ Only For Premium Users-» {zho['premium']} 
{mess_zho}


Want To Go Back!
""" 
    buttons = InlineKeyboardMarkup(row_width = 2)
    buttons.add(InlineKeyboardButton(lang["back"], callback_data="main"))
    with suppress(MessageNotModified, MessageToDeleteNotFound):
        await event.message.edit_text(text, reply_markup=buttons)



###CHARGE##


@register(regexp="charge", user_callback=True, f="cb")
@get_strings_dec("cmds_vars")
async def charge(event,lang):
    shm = await get_status('shm')
    mess_shm = f'⨭ Reason-» {shm["reason"]} \n' if 'reason' in shm else '⨭ Ex-»<code>/shm cc|mm|yy|cvv</code>\n'
    shn = await get_status('shn')
    mess_shn = f'⨭ Reason-» {shn["reason"]} \n' if 'reason' in shn else '⨭ Ex-»<code>/shn cc|mm|yy|cvv</code>\n'
    sha = await get_status('sha')
    mess_sha = f'⨭ Reason-» {sha["reason"]} \n' if 'reason' in sha else '⨭ Ex-»<code>/sha cc|mm|yy|cvv</code>\n'
    shc = await get_status('shc')
    mess_shc = f'⨭ Reason-» {shc["reason"]} \n' if 'reason' in shc else '⨭ Ex-»<code>/shc cc|mm|yy|cvv</code>\n'
    shf = await get_status('shf')
    mess_shf = f'⨭ Reason-» {shf["reason"]} \n' if 'reason' in shf else '⨭ Ex-»<code>/shf cc|mm|yy|cvv</code>\n'
    shl = await get_status('shl')
    mess_shl = f'⨭ Reason-» {shl["reason"]} \n' if 'reason' in shl else '⨭ Ex-»<code>/shl cc|mm|yy|cvv</code>\n'
    shc = await get_status('shc')
    mess_shc = f'⨭ Reason-» {shc["reason"]} \n' if 'reason' in shc else '⨭ Ex-»<code>/shc cc|mm|yy|cvv</code>\n'
    sho = await get_status('sho')
    mess_sho = f'⨭ Reason-» {sho["reason"]} \n' if 'reason' in sho else '⨭ Ex-»<code>/sho cc|mm|yy|cvv</code>\n'
    shi = await get_status('shi')
    mess_shi = f'⨭ Reason-» {shi["reason"]} \n' if 'reason' in shi else '⨭ Ex-»<code>/shi cc|mm|yy|cvv</code>\n'
    csa = await get_status('csa')
    mess_csa = f'⨭ Reason-» {csa["reason"]} \n' if 'reason' in csa else '⨭ Ex-»<code>/csa cc|mm|yy|cvv</code>\n'
    pp = await get_status('pp')
    mess_pp = f'⨭ Reason-» {pp["reason"]} \n' if 'reason' in pp else '⨭ Ex-»<code>/pp cc|mm|yy|cvv</code>\n'
    text = f"""
<b>Ξ Charge gates</b>-
<b>• Total Charge Gates: 10</b>

➥ <b>{shm['name']}</b>-» {shm['status']} || {shm['date']}
⨭ Only For Premium Users-» {shm['premium']} 
{mess_shm}

➥ <b>{sha['name']}</b>-» {sha['status']} || {sha['date']}
⨭ Only For Premium Users-» {sha['premium']} 
{mess_sha}

➥ <b>{shc['name']}</b>-» {shc['status']} || {shc['date']}
⨭ Only For Premium Users-» {shc['premium']}
{mess_shc}

➥ <b>{shf['name']}</b>-» {shf['status']} || {shf['date']}
⨭ Only For Premium Users-» {shf['premium']}
{mess_shf}

➥ <b>{shl['name']}</b>-» {shl['status']} || {shl['date']}
⨭ Only For Premium Users-» {shl['premium']}
{mess_shl}

➥ <b>{sho['name']}</b>-» {sho['status']} || {sho['date']}
⨭ Only For Premium Users-» {sho['premium']}
{mess_sho}

➥ <b>{shi['name']}</b>-» {shi['status']} || {shi['date']}
⨭ Only For Premium Users-» {shi['premium']}
{mess_shi}

➥ <b>{csa['name']}</b>-» {csa['status']} || {csa['date']}
⨭ Only For Premium Users-» {csa['premium']}
{mess_csa}

➥ <b>{shn['name']}</b>-» {shn['status']} || {shn['date']}
⨭ Only For Premium Users-» {shn['premium']}
{mess_shn}

➥ <b>{pp['name']}</b>-» {pp['status']} || {pp['date']}
⨭ Only For Premium Users-» {pp['premium']}
{mess_pp}

Want To Go Back!
""" 
    buttons = InlineKeyboardMarkup(row_width = 2)
    buttons.add(InlineKeyboardButton(lang["back"], callback_data="main"))
    with suppress(MessageNotModified, MessageToDeleteNotFound):
        await event.message.edit_text(text, reply_markup=buttons)



####OTHERS####

@register(regexp="others", user_callback=True, f="cb")
@get_strings_dec("cmds_vars")
# @get_strings_dec("others_cmd")
async def others(event,lang):
    # await event.answer("Soon")
    text = """
<b>Ξ Tools Commands</b>-
<b>• Total Commands: 7</b>

➥ <b>Scrape Cards From Group</b> || Admins only</b>
⨭ Params-» username(username without @)[required] || amount(only digit & amount of cards to scrape)\[required]
⨭ Ex-»<code>.scrapper roldexversechats 100</code>

➥ <b>Bin Information</b>
⨭ Params-» days(must be 6 digits)\[required]
⨭ Ex-»<code>.bin 458595</code>

➥ <b>Redeem Premium Key</b>
⨭ Params-» key\[required]
⨭ Ex-»<code>.redeem key</code>

➥ <b>User Information</b>
⨭ Params-» reply_to_message\[optional]
⨭ Ex-»<code>.info</code>

➥ <b>Get Your Live Saved Cards</b>
⨭ Ex-»<code>.lives</code>

➥ <b>Get Your Claimed Keys</b>
⨭ Ex-»<code>.claimed_keys</code>

➥ <b>Translate Text</b>
⨭ Params-» dest[optional] || text\[required][reply_to_message]
⨭ Ex-»<code>.tr en Te quiero</code>

Want To Go Back!
"""
    buttons = InlineKeyboardMarkup(row_width = 2)
    buttons.add(InlineKeyboardButton(lang["back"], callback_data="main"))
    with suppress(MessageNotModified, MessageToDeleteNotFound):
        await event.message.edit_text(text, reply_markup=buttons)


####SETTINGS####

@register(regexp="settings", user_callback=True, f="cb")
@get_strings_dec("cmds_vars")
@get_strings_dec("settings")
async def settings(event,lang,lang2):
    text = lang2['start_msg']
    buttons = InlineKeyboardMarkup(row_width = 2)
    buttons.add(
        InlineKeyboardButton(lang2["lang"], callback_data="lang"),
        InlineKeyboardButton(lang2["save_cards"], callback_data="save_cards")
                )
    buttons.add(
        InlineKeyboardButton(lang["back"], callback_data="main"),
        InlineKeyboardButton(lang["close"], callback_data="close")
    )
    with suppress(MessageNotModified, MessageToDeleteNotFound):
        await event.message.edit_text(text, reply_markup=buttons)

####LANGUAGES####

@register(regexp="lang", user_callback=True, f="cb")
@get_strings_dec("cmds_vars")
@get_strings_dec("lang")
async def auth(event,lang,lang2):
    text = lang2['start_msg']
    buttons = InlineKeyboardMarkup(row_width = 2)
    buttons.add(
        InlineKeyboardButton("EN(English)", callback_data="set_en"),
        InlineKeyboardButton("HI(Hindi)", callback_data="set_hi"))
    buttons.add(
        InlineKeyboardButton(lang["back"], callback_data="main"),
        InlineKeyboardButton(lang["close"], callback_data="close")
    )
    with suppress(MessageNotModified, MessageToDeleteNotFound):
        await event.message.edit_text(text, reply_markup=buttons)


@register(regexp="set_", user_callback=True, f="cb")
@get_strings_dec("set_lang")
async def auth(event,lang):
    cmd = event.data.split('_')[1]
    if cmd == 'hi':
        await event.answer("Soon")
        return
    x = await change_user_lang(event.message.reply_to_message.from_user.id,cmd)
    with suppress(MessageNotModified, MessageToDeleteNotFound):
        if x:
            await event.message.edit_text(lang['success'])
        else:
            await event.message.edit_text(lang['already'])


@register(regexp="close", user_callback=True, f="cb")
async def close(event):
    # id = event.message.message_id
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound,InvalidQueryID):
        await event.answer("Menu Closed.")
        await event.message.delete()


@get_strings_dec("cmds")
async def start_cmd_new(message, lang):
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action='typing')
        markup = await get_cmds_func(message)
        le = await aioredis.keys('gate_*')
        with suppress(MessageNotModified, MessageToDeleteNotFound):
            await message.edit_text(lang['start_msg'].format(name=message.reply_to_message.from_user.first_name, id=message.reply_to_message.from_user.id,total = len(le)),reply_markup=markup)
    except Exception as e:
        await send_logs(e)


@register(regexp="save_off", user_callback=True, f="cb")
@user_info_callback()
@get_strings_dec("save_off")
async def save_cards(event,user_info,lang):
    message = event.message
    if user_info['save-ccs']:
        x = await adb.users.update_one({'_id': message.from_user.id}, {'$set':{'save-ccs': False}})
        with suppress(MessageNotModified, MessageToDeleteNotFound):
            if x: await event.message.edit_text(lang['success'])
            else: await event.message.edit_text(lang['already'])
    else:
        with suppress(MessageNotModified, MessageToDeleteNotFound):
            await event.message.edit_text(lang['already'])





@register(regexp="save_on", user_callback=True, f="cb")
@user_info_callback()
@get_strings_dec("save_on")
async def save_cards(event,user_info,lang):
    message = event.message
    if not user_info['save-ccs']:
        x = await adb.users.update_one({'_id': message.from_user.id}, {'$set':{'save-ccs': True}})
        with suppress(MessageNotModified, MessageToDeleteNotFound):
            if x: await event.message.edit_text(lang['success'])
            else: await event.message.edit_text(lang['already'])
    else:
        with suppress(MessageNotModified, MessageToDeleteNotFound):
            await event.message.edit_text(lang['already'])


@register(regexp="save_cards", user_callback=True, f="cb")
@user_info_callback()
@get_strings_dec("cmds_vars")
@get_strings_dec("save_cards")
async def save_cards(event,user_info,lang, lang2):
    if user_info['save-ccs']:
        buttons = InlineKeyboardMarkup(row_width = 2)
        buttons.add(InlineKeyboardButton(lang2["turnoff"], callback_data="save_off"))
        buttons.add(InlineKeyboardButton(lang2["back"], callback_data="settings"),InlineKeyboardButton(lang["close"], callback_data="close"))
        with suppress(MessageNotModified, MessageToDeleteNotFound):
            await event.message.edit_text(lang2['start_msg_enabled'], reply_markup = buttons)
    else:
        buttons = InlineKeyboardMarkup(row_width = 2)
        buttons.add(InlineKeyboardButton(lang2["turnon"], callback_data="save_on"))
        buttons.add(
            InlineKeyboardButton(lang2["back"], callback_data="main"),
            InlineKeyboardButton(lang["close"], callback_data="close")
        )
        with suppress(MessageNotModified, MessageToDeleteNotFound):
            await event.message.edit_text(lang2['start_msg_disabled'], reply_markup = buttons)



@register(regexp="main", user_callback=True, f="cb")
async def main_gate(event):
    with suppress(MessageNotModified, MessageToDeleteNotFound):
        await start_cmd_new(event.message)

