from pydantic import BaseModel
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("key not available")

client = Groq(api_key= api_key)
model = "llama-3.3-70b-versatile"
class Ticket(BaseModel):
    name : str
    email : str
    category : str
schema = Ticket.model_json_schema()
response_format = {
    "type" : "Json_object"
}
System_prompt = f"Return output in JSON in format in {schema}"
message_system = {
    "role" : "system",
    "content" : System_prompt
}
text = "Hello my name is harsh , my iphone is not working . I live in lucknow in India and  I used to play cricket daily email is abs@gmail.com and phone number is 423233435"
prompt = f'''This is a customer ticket ,extract customer details from it and text is {text}'''
message_user = {
    "role": "user",
    "content" : prompt
}
messages = [message_system , message_user]
response = client.chat.completions.create(model = model , temperature = 0 , messages = messages)
answer = response.choices[0].message.content
print(answer)