from telethon import TelegramClient
import time

global last_message

# получить свои api_id и hash_id можно на https://my.telegram.org/
api_id = 7232213
api_hash = 'f69e36a1e5c59a8321460c59316bd920'
my_message = '''💊Китайский препарат Lianhua Qingwen - эффективное средство против эпидемического гриппа, лихорадки, озноба, мышечной слабости, заложенности и насморка, кашля, головной боли, сухости и боли в горле.🌡

🦠Капсула Lianhua Qingwen доказала свою эффективность для лечения COVID-19 начальной стадии, включено в китайский протокол лечения COVID-19.🦠

✅Товар прилагается вместе с сертификатами КНР.
💵Цена 250 сом за упаковку (24 капсулы)
📲Телефон / WhatsApp / Telegram для заказа: 0707649142'''  # сообщение которое вы хотите отправлять
path = 'picture.jpg'  # путь или ссылка на картинку
group_id = 1397756569  # id группы, его можно узнать по ссылке группы в веб версии телеграм

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

        time.sleep(5400)


with client:
    client.loop.run_until_complete(main())
