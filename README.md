# NeuroGPT: AI-Powered Telegram Assistant

## 🚀 Overview
NeuroGPT is an asynchronous Telegram bot developed in Python, designed to act as your personal AI assistant. It leverages the power of advanced large language models (LLMs) through the OpenRouter API to provide intelligent and responsive conversational interactions.

## ✨ Features
*   **Asynchronous Architecture:** Built with `aiogram`, ensuring high performance and responsiveness for handling multiple user requests concurrently.
*   **OpenRouter Integration:** Seamlessly connects to OpenRouter, allowing access to a wide range of cutting-edge AI models.
*   **Real-time Typing Indicator:** Provides a "typing..." status in Telegram while the AI generates responses, enhancing user experience.
*   **Secure Configuration:** All sensitive data, such as API keys and bot tokens, are managed securely using environment variables (`.env` file).
*   **Flexible AI Model Selection:** Easily switch between different AI models by updating a single environment variable, enabling quick experimentation and optimization.

## 🤖 Integrated AI Model
By default, NeuroGPT is configured to use the **Meta Llama 3.3 70B Instruct** (`meta-llama/llama-3.3-70b-instruct:free`) model via OpenRouter. This is a powerful and free-to-use model, known for its advanced conversational capabilities.

## 🛠 Setup and Installation

### Prerequisites
*   Python 3.9+
*   A Telegram Bot Token (obtained from @BotFather)
*   An OpenRouter API Key (obtained from OpenRouter.ai)

### Steps
1.  **Clone the repository:**
    ```bash
    git clone <your_repository_url>
    cd NeuroGPT
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure environment variables:**
    Create a file named `.env` in the root directory of your project and add the following:
    ```env
    TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
    OPENAI_API_KEY="YOUR_OPENROUTER_API_KEY"
    AI_MODEL="meta-llama/llama-3.3-70b-instruct:free" # Or any other model available on OpenRouter
    ```
    *Replace `YOUR_TELEGRAM_BOT_TOKEN` and `YOUR_OPENROUTER_API_KEY` with your actual tokens.*

## ▶️ Usage
To start the bot, run:
```bash
python main.py
```
Your bot will now be polling for updates. Send messages to your Telegram bot, and it will respond using the integrated AI model.

## 📄 License
This project is open-source and available under the MIT License.

## 🙏 Credits
*   Developed by [Nivaro]
*   Powered by aiogram and OpenRouter.ai