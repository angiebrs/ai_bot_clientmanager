import os
import requests
from flask import Flask, request

app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

@app.get("/")
def home():
    return "Bot is running!"

@app.post(f"/{TOKEN}")
def webhook():
    data = request.get_json(force=True)
    if not data or "message" not in data:
        return {"ok": True}
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    # Простой ответ-эхо (позже заменим RAG и YClients)
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": f"Вы написали: {text}"}
    )
    return {"ok": True}

if __name__ == "__main__":
    # Render выставит PORT автоматически через переменную окружения
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
