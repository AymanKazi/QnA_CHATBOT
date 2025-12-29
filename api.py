from fastapi import FastAPI, Form
from ollama_client import OllamaClient

app = FastAPI()
ollama = OllamaClient()

@app.get("/")
def home():
    return {"message": "Document Assistant API is running 🚀"}

@app.post("/chat")
def chat(prompt: str = Form(...)):
    # Wrap user input as a message
    messages = [{"role": "user", "content": prompt}]
    response = ollama.chat(messages)
    return {"response": response}
