from ollama_client import OllamaClient

client = OllamaClient()

conversation = [
    {
        "role": "system",
        "content": (
            "You are a helpful, friendly chatbot. "
            "Answer clearly and politely. "
            "Do not ask unnecessary follow-up questions."
        )
    }
]

print("\n💬 Chatbot started (type 'exit' to quit)\n")

while True:
    user_input = input("Enter your message: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    conversation.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat(conversation)

    print("\nBOT:", response, "\n")

    conversation.append({
        "role": "assistant",
        "content": response
    })
