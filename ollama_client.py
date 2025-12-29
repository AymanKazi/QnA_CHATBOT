# ollama_client.py
import requests
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base = base_url

    def chat(self, messages, temperature=0.3, max_tokens=200):
        """
        messages: list of {"role": "user"|"assistant", "content": "text"}
        Returns full response as string
        """
        url = f"{self.base}/api/chat"
        payload = {
            "model": "llama3.2",
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False
        }

        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()

            # Standard chat response
            if "message" in data and "content" in data["message"]:
                return data["message"]["content"]

            # Fallback
            if "response" in data:
                return data["response"]

            return str(data)

        except requests.exceptions.ConnectionError:
            return f"Error: Cannot connect to Ollama at {self.base}"
        except Exception as e:
            return f"Error: {str(e)}"
