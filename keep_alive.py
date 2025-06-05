from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Використовуємо PORT з Render або 5000 за замовчуванням
    app.run(host='0.0.0.0', port=port)
