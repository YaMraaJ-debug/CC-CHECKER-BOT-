# from jocasta import bot, dp
# from jocasta.dec import register
# from jocasta.services.language import get_strings_dec
# from jocasta.services.get_chat_settings import get_chat_dec


# @register(f = 'welcome')
# @get_strings_dec("new_chat_participant")
# @get_chat_dec()
# async def new_chat_participant(message, lang, chat_info):
#     print(message)
#     if chat_info['new_chat_participant'] is False:
#         return
#     print(message)
#     message.reply(
#         lang['message'].format(
#             name =message.new_chat_participant.first_name,
#             id = message.new_chat_participant.id
#         )
#     )

