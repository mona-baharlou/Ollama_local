import requests
import json

#base url for local ollama
url = "http://localhost:11434/api/chat"


#Payload
payload = {
    "model" : "llama3.2",
    "messages": [{"role":"user", "content":"What is Kotlin?"}]

}

response = requests.post(url, json=payload, stream=True)

#check response
if response.status_code == 200:
    print("Streaming resonse from ollama")
    for line in response.iter_lines(decode_unicode=True):
        if line: #ignore empty lines
            try:
                #Parse each line as a json obj
                json_data = json.loads(line)
                #Extract and print the assistant's message content
                if "message" in json_data and "content" in  json_data["message"]:
                 print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
               print(f"\nFailed to parse line: {line}")
    print() #ensure the final output ends with a newline
else:
   print(f"\n Error: {response.status_code}")
   print(response.text)
