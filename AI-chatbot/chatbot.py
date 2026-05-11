import requests

MODEL = "phi3"

def get_response(messages):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False
        }
    )
    return response.json()["message"]["content"]