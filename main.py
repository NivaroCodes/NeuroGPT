import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, flags
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.chat_action import ChatActionMiddleware
from openai import AsyncOpenAI

logging.basicConfig(level=logging.INFO)
load_dotenv()

token = os.getenv("TOKEN")
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp.message.middleware(ChatActionMiddleware())

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

@dp.message(Command("start"))
async def start_bot(message: types.Message):
    await message.answer(
        "Привет! Я NeuroGPT, твой персональный ассистент"
    )

@dp.message(lambda message: message.text)
@flags.chat_action("typing")
async def create_ai(message: types.Message):
    completion = await client.chat.completions.create(
        model=os.getenv("AI_MODEL", "meta-llama/llama-3.3-70b-instruct:free"),
        messages=[{"role": "user", "content": message.text}]
    )

    text = completion.choices[0].message.content
    await message.answer(text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
