import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Key not available")

client = Groq(api_key=api_key)

model = "llama-3.3-70b-versatile"
role = "user"
prompt = "Suggest a name"
message_system = {
    "role": "system",
    "content": "Your are a brand manager suggest name for my clothing brand"
}
message = {
    "role": role,
    "content": prompt
}
messages = [message_system,message]
response = client.chat.completions.create(model=model , messages=messages, temperature=2)
# print(response)

print("############################################################")
answer = response.choices[0].message.content
print(answer)
