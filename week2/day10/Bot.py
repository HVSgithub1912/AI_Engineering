from groq import Groq
import os 
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
model = "llama-3.3-70b-versatile"
my_key = os.getenv("GROQ_API_KEY")
if not my_key:

    raise ValueError("key not available...")
    print("-"*10)
client = Groq(api_key= my_key)
