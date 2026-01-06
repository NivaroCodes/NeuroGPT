import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from openai import OpenAI

TOKEN = "8595740921:AAEgDvYXXokGgejLwNrUqxc6Nh9baMDC9w0"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_bot(message: types.Message):
  await message.reply("Привет! Я NeuroGPT, твой личный ассистент по любым вопросам.")

@dp.message(lambda message: message.text)
async def create_ai(message: types.Message):
  client = OpenAI(
  base_url="https://api.langdock.com/openai/eu/v1",
  api_key="sk-4q72nZ7wciGNntRS0pPfl2nYnR3S1GNShNmsDa2XpVSoRv1WyAsGvkgYfn9iy3QPMGWDxwHhmo9CGysXIChMNg"
)

  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "user", "content": message.text}
    ]
)
  text = completion.choices[0].message.content
  await message.answer(text)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")