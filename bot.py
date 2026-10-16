import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8817825578:AAFxfd2h0GrYKIaM7wRKoFQoXYc9HA0jP0Q"
WEB_APP_URL = "SINI_VEYA_GITHUP_PAGES_LINKINIZ_BURAYA_YAZILSIN/index.html"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    args = message.text.split()
    ref_id = args[1] if len(args) > 1 else None
    
    if ref_id:
        # Burada referal məntiqini yaza və ya Firebase-ə qeyd edə bilərsən
        print(f"İstifadəçi {message.from_user.id} referal ilə gəldi: {ref_id}")

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Botu Başlat", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    
    await message.answer(
        "Salam! Reklama baxaraq qazanmaq üçün aşağıdakı düyməyə basın və Mini App-i açın.",
        reply_markup=markup
    )

if __name__ == "__main__":
    import asyncio
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
