import requests
import json
from time import sleep
def run_test(text):
    url = "http://localhost:5005/webhooks/rest/webhook"
    response = requests.post(url, data=json.dumps({"sender": "default", "message":text}))
    print(response.json()[0]["text"])

run_test("")
sleep(2)

