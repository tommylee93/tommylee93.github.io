from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.utils import executor
import logging

TOKEN = "7499818544:AAEehBYH5cSLemi9jBz2DMuabdUuy_JjqJY"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="Apri WebApp", web_app=WebAppInfo(url="https://tommylee93.github.io"))
    keyboard.add(button)
    await message.answer("Clicca sul pulsante per aprire la WebApp:", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
