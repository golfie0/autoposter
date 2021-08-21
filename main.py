from telethon import TelegramClient
import time

global last_message

# получить свои api_id и hash_id можно на https://my.telegram.org/
api_id = 7013458
api_hash = '97d6c50f9d8f98e597b6b4b4af62f40fё'
my_message = '''💊Китайский препарат Lianhua Qingwen - эффективное средство против эпидемического гриппа, лихорадки, озноба, мышечной слабости, заложенности и насморка, кашля, головной боли, сухости и боли в горле.🌡

🦠Капсула Lianhua Qingwen доказала свою эффективность для лечения COVID-19 начальной стадии, включено в китайский протокол лечения COVID-19.🦠

✅Товар прилагается вместе с сертификатами КНР.
💵Цена 250 сом за упаковку (24 капсулы)
📲Телефон / WhatsApp / Telegram для заказа: 0707649142'''  # сообщение которое вы хотите отправлять
path = 'picture.jpg'  # путь или ссылка на картинку
group_id = 552348599  # id группы, его можно узнать по ссылке группы в веб версии телеграм

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    None


async def main():
    group = await client.get_entity(group_id)
    while True:
        async for message in client.iter_messages(group, limit=1):
            last_message = message

        if my_message != last_message.text:
            await client.send_message(group, my_message, file=path)

        time.sleep(10)


with client:
    client.loop.run_until_complete(main())
