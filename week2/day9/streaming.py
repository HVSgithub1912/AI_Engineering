from groq import Groq
import os 
from dotenv import load_dotenv
load_dotenv()
model = "llama-3.3-70b-versatile"
my_key = os.getenv("GROQ_API_KEY")
if not my_key:
    raise ValueError("key not available")

client = Groq(api_key= my_key)
user_prompt = f"""Tell me about networking company akamai."""

def ask_llm(user_prompt):
    user_message = {
        "role": "user",
        "content": user_prompt
    }
    #This one is older way 
    messages = [user_message]
    # response = client.chat.completions.create(messages=messages , model=model, temperature=0)
    # answer = response.choices[0].message.content
    # print(answer)

    stream = client.chat.completions.create(model=model, messages=messages, stream=True)
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end=" " , flush=True)

ask_llm(user_prompt)