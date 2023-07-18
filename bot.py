import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, exceptions

TOKEN = "6313877286:AAHrl52fjthsyREAGh1etzvUFCnAK6fYL6Y"
CHAT_ID = "800695035"
URL = "https://paraai.pro"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_message(text):
    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text=text)
            break
        except exceptions.NetworkError:
            print(f"Network error occurred while trying to send message: {text}")
            await asyncio.sleep(5)

async def ping_website():
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(URL) as response:
                    if response.status == 200:
                        await send_message(f"Website \u2705 {URL} is up.")
                    else:
                        await send_message(f"Website \u274C {URL} is down. Status code: {response.status}")
        except Exception as e:
            await send_message(f"An error occurred while trying to ping {URL}: {str(e)}")
        await asyncio.sleep(300)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ping_website())
