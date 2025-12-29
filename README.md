<<<<<<< HEAD
# QnA Chatbot

A **FastAPI-based QnA Chatbot** powered by **Ollama LLM**.  
This project allows users to interact with an AI chatbot via a web API or Swagger UI.

---

## Features

- Chat with the AI using natural language.
- Supports multiple queries in a single session.
- Easy-to-use **Swagger UI** for testing endpoints.
- Built using **FastAPI** for high performance and simplicity.
- Ollama LLM integration for generating intelligent responses.

---

## Requirements

- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://docs.python-requests.org/en/latest/)
- Ollama LLM running locally

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/QnA_CHATBOT.git
cd QnA_CHATBOT
Create and activate a virtual environment

bash
Copy code
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Make sure Ollama server is running locally

bash
Copy code
ollama serve
Running the Chatbot
Start the FastAPI server:

bash
Copy code
python -m uvicorn api:app --reload
Open your browser and go to:

arduino
Copy code
http://127.0.0.1:8000/docs
Use the /chat endpoint to send your queries.

Example POST payload:

json
Copy code
{
  "prompt": "Hello, tell me a joke"
}
Project Structure
graphql
Copy code
QnA_CHATBOT/
│
├── api.py              # FastAPI app with chat endpoints
├── ollama_client.py    # Handles communication with Ollama API
├── app.py              # Optional CLI version of chatbot
├── requirements.txt    # Python dependencies
├── README.md
└── .venv/              # Virtual environment (ignored in Git)
Usage Example
Send a prompt via Swagger UI or API client.

Get intelligent responses from the AI chatbot.

Example session:

vbnet
Copy code
User: Tell me a joke
Bot: Why did the chicken cross the road? To get to the other side!
=======
# QnA_CHATBOT
A FastAPI-based QnA Chatbot using Ollama LLM
>>>>>>> f54a247d0c0ea120194329fcb4464fbb5279caac
