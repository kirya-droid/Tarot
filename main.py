import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv
import os
from tarot import get_tarot_reading

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher()

# Приветствие и кнопка WebApp
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text="🔮 Получить расклад Таро", web_app=WebAppInfo(url="https://kirya-droid.github.io/Tarot/tarot_webapp/")))
    await message.answer("👋 Привет! Нажми на кнопку ниже и получи свой расклад Таро!", reply_markup=kb.as_markup(resize_keyboard=True))

# Обработка данных из WebApp
@dp.message(F.web_app_data)
async def web_app_tarot(message: types.Message):
    user_data = message.web_app_data.data.split("|")
    user_name, user_birthdate, user_question = user_data[0], user_data[1], user_data[2]

    await message.answer("🔮✨ Минутку, делаю для тебя расклад...")

    tarot_result = await get_tarot_reading(user_name, user_birthdate, user_question)

    await message.answer(f"✨ Вот твой расклад, {user_name}:\n\n{tarot_result}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.run_polling(bot)
