import requests

url = "http://127.0.0.1:11434/api/generate"

data = {
    "model": "gemma3:1b",
    "prompt": "nvidia는 어떤 회사야?",
    "stream": False
}

response = requests.post(url, json=data)
response.raise_for_status()

result = response.json()

print("=== LLM Response ===")
print(result["response"])
