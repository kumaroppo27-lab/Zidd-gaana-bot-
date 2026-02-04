# ----------------- Dummy Flask server for Render free tier -----------------
from flask import Flask
import threading
import os

dummy_app = Flask(__name__)

@dummy_app.route('/')
def home():
    return "Bot is alive! 🚀", 200

@dummy_app.route('/health')
def health():
    return "OK", 200

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))  # Render $PORT use karega, fallback 10000
    dummy_app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

# Start dummy server in background thread (bot blocking na ho)
threading.Thread(target=run_dummy_server, daemon=True).start()

# Ab yahan se tumhara original bot start code chalta rahega
# jaise: app.start() ya client.run() ya idle()
