import asyncio
import requests
from aiogram import Bot, Dispatcher

TOKEN = "6313877286:AAHrl52fjthsyREAGh1etzvUFCnAK6fYL6Y"
CHAT_ID = "800695035"
URL = "https://beta.paraai.pro"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def ping_website():
    while True:
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                await bot.send_message(chat_id=CHAT_ID, text=f"Website {URL} is up.")
            else:
                await bot.send_message(chat_id=CHAT_ID, text=f"Website {URL} is down. Status code: {response.status_code}")
        except requests.RequestException as e:
            await bot.send_message(chat_id=CHAT_ID, text=f"An error occurred while trying to ping {URL}: {str(e)}")
        await asyncio.sleep(30)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ping_website())
