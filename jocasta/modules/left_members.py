# from jocasta import bot, dp
# from jocasta.dec import register
# from jocasta.services.language import get_strings_dec
# from jocasta.services.get_chat_settings import get_chat_dec


# @register(f = 'leave')
# @get_strings_dec("left_chat_participant")
# @get_chat_dec()
# async def left_chat_participant(message, lang, chat_info):
#     if chat_info['left_chat_participant'] is False:
#         return
#     message.reply(
#         lang['message'].format(
#             name = message.left_chat_participant.first_name,
#             id = message.left_chat_participant.id
#         )
#     )



# __mod__ = "Left Chat Participant"

# __help__ = "Gives message of left members."

