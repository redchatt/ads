import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Sənin Tokenin və GitHub Pages linkin
TOKEN = "8817825578:AAH1_BplDCGUp9sTU3S40KmBH0xkQTT1wE4"
WEB_APP_URL = "https://redchatt.github.io/ads/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    args = message.text.split()
    ref_id = args[1] if len(args) > 1 else ""
    
    final_url = f"{WEB_APP_URL}?start={ref_id}" if ref_id else WEB_APP_URL

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Tətbiqi Başlat", web_app=WebAppInfo(url=final_url))]
    ])
    
    await message.answer(
        f"Xoş gəldiniz, {message.from_user.first_name}!\n\n"
        "Vortex Ads vasitəsilə reklam izləyərək, hədiyyə qutuları açaraq və tapşırıqları yerinə yetirərək qazanmağa başlayın.",
        reply_markup=markup
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
