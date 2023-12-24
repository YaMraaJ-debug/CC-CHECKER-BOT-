from datetime import datetime
from jocasta import USERNAME
from pyrogram import Client, filters
from jocasta.services.addtodb import pyro_user_info_dec
from jocasta.services.language import get_strings_dec
from jocasta.services.pyro import pbot
from jocasta.utlis.send_log import send_logs

@pbot.on_message(filters.command(["info", f'info{USERNAME}'], prefixes=[".", "/", "!", '?'], case_sensitive=False) & filters.text)
@get_strings_dec("info")
@pyro_user_info_dec()
async def info(Client, message,strings, user):
    try:
        await message.reply_chat_action("typing")
        lastmessage = message.from_user.last_name if message.from_user.last_name is not None else ''
        chat_user_name = 'Private' if message.chat.username is None else message.chat.username
        chat_name = message.chat.first_name if message.chat.first_name is not None else message.chat.title
        if message.reply_to_message is not None and message.reply_to_message.from_user.id != message.from_user.id:
            lastmessage = message.reply_to_message.from_user.last_name if message.reply_to_message.from_user.last_name is not None else ''
            messagetext = f"""
<b>{strings['name']}</b>:-
<b>{strings['firstname']}</b>: <b>{message.reply_to_message.from_user.first_name} {lastmessage}</b>
<b>{strings['username']}</b>: @<b>{message.reply_to_message.from_user.username}</b>
<b>{strings['userid']}</b>: <code>{message.reply_to_message.from_user.id}</code>
<b>{strings['restricted']}</b>: <b>{message.reply_to_message.from_user.is_restricted}</b>
<b>{strings['scamtag']}</b>: <b>{message.reply_to_message.from_user.is_scam}</b>
<b>{strings['fakeuser']}</b>: <b>{message.reply_to_message.from_user.is_fake}</b>
<b>{strings['link']}</b>: [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id})
<b>{strings['chatid']}</b>: <code>{message.reply_to_message.chat.id}</code>
<b>{strings['chatname']}</b>: <b>{chat_name}</b>
<b>{strings['chatusername']}</b>: <b>{chat_user_name}</b>
<b>{strings['chattype']}</b>: <b>{message.reply_to_message.chat.type.title()}</b>
"""
        elif user['status'] == 'F':
            messagetext = f"""
<b>{strings['name']}</b>:-
<b>{strings['firstname']}</b>: <b>{message.from_user.first_name} {lastmessage}</b>
<b>{strings['username']}</b>: @<b>{message.from_user.username}</b>
<b>{strings['userid']}</b>: <code>{message.from_user.id}</code>
<b>{strings['restricted']}</b>: <b>{message.from_user.is_restricted}</b>
<b>{strings['scamtag']}</b>: <b>{message.from_user.is_scam}</b>
<b>{strings['fakeuser']}</b>: <b>{message.from_user.is_fake}</b>
<b>{strings['link']}</b>: [{message.from_user.first_name}](tg://user?id={message.from_user.id})
<b>{strings['chatid']}</b>: <code>{message.chat.id}</code>
<b>{strings['chatname']}</b>: <b>{chat_name}</b>
<b>{strings['plan']}</b>: <b>{user['role']} User</b>
<b>{strings['reg_time']}</b>: <b>{user['reg-date']}</b>
<b>{strings['antispam_time']}</b>: <b>{user['spam-time']} Sec's</b>
<b>{strings['save_ccs']}</b>: <b>{user['save-ccs']}</b>
<b>{strings['chatusername']}</b>: <b>{chat_user_name}</b>
<b>{strings['chattype']}</b>: <b>{message.chat.type.title()}</b>
"""
        else:
            x = datetime.fromtimestamp(user['expiry'])
            messagetext = f"""
<b>{strings['name']}</b>:-
<b>{strings['firstname']}</b>: <b>{message.from_user.first_name} {lastmessage}</b>
<b>{strings['username']}</b>: @<b>{message.from_user.username}</b>
<b>{strings['userid']}</b>: <code>{message.from_user.id}</code>
<b>{strings['restricted']}</b>: <b>{message.from_user.is_restricted}</b>
<b>{strings['scamtag']}</b>: <b>{message.from_user.is_scam}</b>
<b>{strings['fakeuser']}</b>: <b>{message.from_user.is_fake}</b>
<b>{strings['link']}</b>: [{message.from_user.first_name}](tg://user?id={message.from_user.id})
<b>{strings['chatid']}</b>: <code>{message.chat.id}</code>
<b>{strings['chatname']}</b>: <b>{chat_name}</b>
<b>{strings['plan']}</b>: <b>{user['role']} User</b>
<b>{strings['rem_days']}</b>: <b>{user['expiry_days']} Days</b>
<b>{strings['exp_date']}</b>: <b>{x}</b>
<b>{strings['reg_time']}</b>: <b>{user['reg-date']}</b>
<b>{strings['antispam_time']}</b>: <b>{user['spam-time']} Sec's</b>
<b>{strings['save_ccs']}</b>: <b>{user['save-ccs']}</b>
<b>{strings['chatusername']}</b>: <b>{chat_user_name}</b>
<b>{strings['chattype']}</b>: <b>{message.chat.type.title()}</b>
"""
        await message.reply(messagetext, quote= True)
    except Exception as e:
        await send_logs(e)