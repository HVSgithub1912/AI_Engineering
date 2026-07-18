from groq import Groq
import os
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key= api_key)


