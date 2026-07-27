from groq import Groq
import os 
from dotenv import load_dotenv
load_dotenv()
model = "llama-3.3-70b-versatile"
my_key = os.getenv("GROQ_API_KEY")
if not my_key:

    raise ValueError("key not available...")
    print("-"*10)
client = Groq(api_key= my_key)
# tools for my LLM
def price_decider(product):
    if product=="paties":
        return 20
    elif product == "samosa":
        return 10
    else:
        return 0

def calculator(a , b):
    return a - b;


tools = {
    "price_decider" : price_decider,
    "calculator" : calculator
}


system_prompt = f"""You are a expanse tracker
You have  tools like:
price_decider(product)
calculator(a , b)
IMPORTANT:
use this tools exactly in way defined below :
ACTION: price_decider("paties")
ACTION: calculator(500 , 20)
Don't:
price_decider(product = "paties")
calculator(a = 200 , b = 20)
FOLLOW THESE RULES
1. decide what to do next 
2. use the best fit tools for that problem
3. wait after using the tool
4. take the observation
5. no need to invent any solution by your own 
6. use that observation for next operation (if needed )
Format:

Thought: what you need to do
Action: tool_name(argument)

When finished:

Final Answer: your answer
"""


user_prompt = f"""
I bought 3 somasas from the college canteen one for me and two for my girlfriend named kratika . Initially I have 500 rupees 
how much money is left after purchasing samosa if one samosa cost : 20 rupees.
"""
def llm_call():
    user_message = {
        "role": "user",
        "content" : user_prompt
    }
    system_message = {
        "role": "system",
        "content": system_prompt
    }
    messages = [user_message, system_message]
    response = client.chat.completions.create(model=model , messages=messages , temperature= 0)
    answer = response.choices[0].message.content
    print(answer)

llm_call()