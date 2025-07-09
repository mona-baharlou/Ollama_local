This is a simple Python script to interact with the locally hosted Ollama API (chat endpoint) using the llama3.2 model. It sends a user prompt and streams the response from the model in real time.

# Features
- Connects to http://localhost:11434/api/chat
- Sends a user message to the LLaMA3.2 model
- Streams the assistant's response line by line
- Handles and parses JSON responses
- Gracefully handles empty lines and JSON decoding errors

# Requirements
- Python 3.7+
- requests library (install with pip install requests)
- A running instance of Ollama with the llama3.2 model installed

# Usage
- Start your local Ollama server and ensure the llama3.2 model is available.
- Run the script:

