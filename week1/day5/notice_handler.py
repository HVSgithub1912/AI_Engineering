from groq import Groq
import os
import time
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"
application = f"""**Date:** 19 July 2026

**To**
The Principal
St. Joseph Modern School

**Subject: Application for School Leaving Certificate Due to Father's Transfer**

Respected Sir/Madam,

I am **Harry**, a student of **Class 9-A**, **Roll No. 32**, studying at St. Joseph Modern School. I respectfully request you to issue my School Leaving Certificate and other necessary school documents.

My father has been officially transferred from **Lucknow to New Delhi**, and our family will be relocating there shortly. Due to this transfer, I will not be able to continue my studies at your esteemed school.

I kindly request you to process my application and issue my Transfer Certificate, School Leaving Certificate, and any other required documents at the earliest so that I may complete my admission formalities at my new school.

Thank you for your support and cooperation.

Yours obediently,

**Harry**
Class: 9-A
Roll No.: 32
Phone No.: 34342452552
"""
class Application(BaseModel):
    Name : str| None
    Roll_no : int | None
    Class : str | None
    Sec : str | None
    Subject : str 
    Phone_no : str|None



Application_schema = Application.model_json_schema()


System_prompt = f"""
You are the management head of a school.

Your task is to extract information from the student's application.

Return ONLY a valid JSON object.

The JSON must strictly follow this schema:

{Application_schema}

If any field is missing, return null.

Do not return markdown.
Do not return explanations.
"""


user_prompt = f'''Summarize the application : {application}'''

message_user = { 
    'role': 'user',
    'content': user_prompt
}
message_system = {
    'role' : 'system',
    'content': System_prompt
}
response_format = {
    "type": "json_object"
}
messages = [message_system, message_user]
response = client.chat.completions.create(model = model, messages = messages, response_format = response_format)
answer = response.choices[0].message.content
# print(answer)
print(type(answer)) 

