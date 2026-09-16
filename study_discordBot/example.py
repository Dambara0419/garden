import os
import requests
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# os.getenv() で値を取得する
# api_key = os.getenv("API_KEY")
# db_url = os.getenv("DATABASE_URL")
# debug_mode = os.getenv("DEBUG")

WEBHOOK_URL = os.getenv("WEB_HOOK_URL")
data = {"content": "こんにちは！システムからの通知です！"}

requests.post(WEBHOOK_URL, json=data)