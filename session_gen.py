try: 
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient
except:
    print("You didnt installed telethon. I am installing......")
    import os
    
    os.system("pip install telethon")
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

try:
    API_ID = int(input("Tell Me Your Api Id: "))
except ValueError:
    print("Only Integer are allowed")

API_HASH = str(input("Tell Me Your Api Hash: "))


with TelegramClient(StringSession(), api_id= API_ID, api_hash = API_HASH) as client:
    session = client.session.save()
    text = f"""
This is you session hash copy and don't send it to anyone
`{session}`
Api Made By: [Roldex](https://t.me/r0ld3x)
Github: [Roldex](https://www.github.com/r0ld3x)"""
    client.send_message("me",text)
    print(session)
    print("This is you session string copy with carefully. and one of this is sent to your account's save message")