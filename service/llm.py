import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"

async def ask_llm(prompt: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            OLLAMA_URL,
            json={
                "model": "ministral-3:3b",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]