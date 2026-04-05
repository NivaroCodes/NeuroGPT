# NeuroGPT: Local AI Telegram Assistant

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![Ollama](https://img.shields.io/badge/AI-Ollama-orange.svg)

## 🚀 Overview

**NeuroGPT** is an asynchronous Telegram bot built with Python that acts as a local AI assistant. Unlike cloud-based solutions, it runs entirely on your machine using a local LLM via **Ollama**, providing full control over data and zero dependency on external APIs.

This project is designed as a practical backend + AI integration project, demonstrating how to connect LLMs to real-world applications.

---

## ✨ Features

* **Asynchronous Architecture**: Built with `aiogram` for efficient concurrent message handling.
* **Local AI Inference (Ollama)**: Runs fully offline using a local language model.
* **Low Latency Responses**: No external API calls → faster response time (depending on your hardware).
* **Telegram UX Enhancements**:
    * Real-time "typing..." indicator.
    * Clean and structured responses.
* **Secure Configuration**: Sensitive data is stored securely in a `.env` file.
* **Flexible Model Switching**: Easily change models via a single variable.

---

## 🧠 AI Model

**Default model:** `ministral-3:3b`

**Specifications:**
* **Parameters:** ~3B
* **Size:** ~3GB
* **Capabilities:** Multilingual support, optimized for local/edge deployment.

---

## 🏗 Architecture

The flow of information in the system:
`Telegram` ➔ `aiogram bot` ➔ `Ollama (localhost:11434)` ➔ `LLM` ➔ `Response`

---

## 📈 Future Improvements

- [ ] **Conversation memory**: Implement context/history for dialogue.
- [ ] **Response caching**: Speed up repeated queries.
- [ ] **Rate limiting**: Prevent bot spam.
- [ ] **Webhook support**: For better production scalability.
- [ ] **Cloud deployment**: Support for remote API models (OpenAI, Anthropic).

---

## 📄 License

Distributed under the **MIT License**.

---

## 👨‍💻 Author

Developed by **Nivaro**

> [!TIP]
> **Note:** This project is intended as a pet project for backend + AI integration practice and as a foundation for future production AI systems.


## 🛠 Setup and Installation

### Prerequisites
* Python 3.9+
* [Ollama](https://ollama.com) installed and running
* Telegram Bot Token (from [@BotFather](https://t.me/botfather))

### 1. Install Ollama
Download and install from the official site. Then, pull the required model:
```bash
# Start the server (if not running as a service)
ollama serve

# Pull the default model
ollama pull ministral-3:3b
