from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging

TOKEN = "HHHHHHHHHHHH"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(
        text="Apri WebApp", 
        web_app=WebAppInfo(url="https://tommylee93.github.io/")
    )
    keyboard.add(button)
    
    await message.answer("Clicca sul pulsante per aprire la WebApp:", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentTypes.WEB_APP_DATA)
async def webapp_data(message: types.Message):
    await message.answer(f"Hai inviato: {message.web_app_data.data}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
