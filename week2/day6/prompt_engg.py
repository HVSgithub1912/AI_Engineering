from groq import Groq
from dotenv import load_dotenv
import os
from pydantic import BaseModel
load_dotenv()

key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=key)
model ="llama-3.3-70b-versatile"
class service(BaseModel):
    name : str | None
    device_name : str | None
    issue : str | None


system_prompt = f'''
Your are a manager at smartphone service center
#Task:
1. Divide the user issue into the given category:
(technical issue , hardware repair)
#constraint:
1. Don't no categorize by your own 
#roll_back:
if the issue is not related to technical or hardware of smartphone the return none
'''
system_message = {
    "role": "system",
    "content": system_prompt
}
user_prompt = '''My boyfriend cheated on me , I am upset and i want a new one '''
user_message = {
    "role" : 'user',
    'content': user_prompt
}




messages = [user_message,system_message]
response = client.chat.completions.create(messages= messages , model = model)
answer = response.choices[0].message.content
print(answer)