# email_processor/chatgpt/ops.py

import requests

from email_processor.config import CHATGPT_ENDPOINT, CHATGPT_API_KEY
import time

def send_to_chatgpt(content):
    time.sleep(1)  # Simple delay. Adjust according to your API quota.
    # Send content to ChatGPT and get the response
    # ...

def interact_with_chatgpt(content):
    """Send the content to ChatGPT and get a response."""
    headers = {"Authorization": f"Bearer {CHATGPT_API_KEY}"}
    response = requests.post(CHATGPT_ENDPOINT, json={"messages": [{"role": "system", "content": content}]}, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error from ChatGPT: {response.text}")
