import requests

WEBHOOK_URL = "ここにコピーしたURLを貼り付けます"
data = {"content": "こんにちは！システムからの通知です！"}

requests.post(WEBHOOK_URL, json=data)