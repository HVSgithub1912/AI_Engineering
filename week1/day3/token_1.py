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
prompt1 = "hello"
prompt2 = "Explain about rainforest"
prompt3 = "give a 1000 word essay on desalation of sea water"
prompts = [prompt1,prompt2,prompt3]
messages = []

for prompt in prompts:

    message = {
        "role": role,
        "content": prompt
    }    
    messages.append(message)
   
    response = client.chat.completions.create(model=model , messages=messages, temperature=0 , max_tokens=100)
    usage = response.usage
    print(f"Prompt : {prompt} --> your tokens {usage.prompt_tokens} , completion token --> {usage.completion_tokens}, total_token --> {usage.completion_tokens} Finish_reason : {response.choices[0].finish_reason}")
  