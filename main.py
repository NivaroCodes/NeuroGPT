import os
import asyncio
import logging
import httpx
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, flags
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.chat_action import ChatActionMiddleware

logging.basicConfig(level=logging.INFO)
load_dotenv()

token = os.getenv("TOKEN")

bot = Bot(
    token=token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()
dp.message.middleware(ChatActionMiddleware())

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "ministral-3:3b"


@dp.message(Command("start"))
async def start_bot(message: types.Message):
    await message.answer("Привет! Я NeuroGPT, локальный ассистент.")


@dp.message(lambda message: message.text)
@flags.chat_action("typing")
async def create_ai(message: types.Message):

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are NeuroGPT, a Telegram assistant. "
                            "ALWAYS respond in Telegram HTML format. "
                            "NEVER use markdown (** or __). "
                            "Use <b>, <i>, and bullet points."
                        )
                    },
                    {
                        "role": "user",
                        "content": message.text
                    }
                ],
                "stream": False,
                "options": {
                    "num_predict": 300
                }
            }
        )

    data = response.json()
    logging.info(f"Ollama response: {data}")

    text = data.get("message", {}).get("content", "").strip()

    if not text:
        text = "⚠️ Модель не ответила. Попробуйте ещё раз."

    await message.answer(text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())