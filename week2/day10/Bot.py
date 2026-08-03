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



resume = f"""# **Harsh Vardhan Singh**

📍 Kanpur, UP | 📞 +91-9648888802 | Email: harsh.v.s.1021@gmail.com
🔗 LinkedIn: linkedin.com/in/yourprofile | GitHub: github.com/HVSgithub1912 | Portfolio: yourportfolio.com

## PROFESSIONAL SUMMARY

Generative AI Engineer with experience in building AI-powered applications using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), AI agents, and prompt engineering. Proficient in Python, LangChain, OpenAI APIs, vector databases, and cloud platforms. Strong background in developing scalable AI solutions, integrating LLMs into enterprise workflows, and deploying production-ready machine learning applications.

## TECHNICAL SKILLS

**Programming:** Python, SQL, JavaScript

**Generative AI:**

* GPT-4/5, Claude, Gemini, Llama
* Prompt Engineering
* Retrieval-Augmented Generation (RAG)
* AI Agents
* Function Calling
* Fine-tuning Concepts

**Frameworks & Libraries:**

* LangChain
* LangGraph
* LlamaIndex
* Hugging Face Transformers
* OpenAI SDK
* FastAPI
* Streamlit
* Gradio

**Vector Databases:**

* Pinecone
* ChromaDB
* FAISS
* Weaviate

**Machine Learning:**

* Scikit-learn
* PyTorch
* TensorFlow
* Pandas
* NumPy

**Cloud & DevOps:**

* AWS
* Azure OpenAI
* Docker
* GitHub Actions
* Kubernetes (Basics)

**Databases:**

* PostgreSQL
* MongoDB
* Redis

---

## PROFESSIONAL EXPERIENCE

### Generative AI Engineer

Code Alpha | Jan 2024 – Present

* Developed enterprise-grade RAG applications using LangChain and OpenAI GPT models.
* Built AI chatbots capable of answering domain-specific questions with over 90% response accuracy.
* Designed prompt engineering strategies to improve response quality and reduce hallucinations.
* Integrated vector databases (Pinecone/ChromaDB) for semantic search and document retrieval.
* Developed REST APIs using FastAPI for AI model deployment.
* Automated document processing pipelines using LLMs and OCR.
* Optimized inference costs through prompt optimization and caching.

**Technologies:** Python, OpenAI API, LangChain, Pinecone, FastAPI, Docker

---

### AI/ML Engineer

TechBird | Jun 2022 – Dec 2023

* Built NLP models for text classification and summarization.
* Created data preprocessing pipelines for large datasets.
* Deployed ML models using Docker and cloud infrastructure.
* Worked closely with product teams to integrate AI capabilities into web applications.

---

## PROJECTS

### Enterprise RAG Chatbot

* Built an intelligent chatbot using LangChain, OpenAI GPT, and Pinecone.
* Enabled document-based question answering from PDFs and enterprise knowledge bases.
* Reduced information retrieval time by 80%.

**Tech Stack:** Python, LangChain, OpenAI, Pinecone, FastAPI

---

### AI Resume Analyzer

* Developed an LLM-based resume screening application.
* Implemented semantic matching between resumes and job descriptions.
* Generated ATS scores and personalized improvement suggestions.

**Tech Stack:** Python, GPT-4, Streamlit, ChromaDB

---

### Multi-Agent Research Assistant

* Built a multi-agent workflow using LangGraph.
* Automated web research, summarization, and report generation.
* Integrated external APIs for real-time information retrieval.

---

## EDUCATION

**Bachelor of Technology (B.Tech.)**
University Name | Year

---

## CERTIFICATIONS

* Microsoft Azure AI Engineer Associate
* AWS Certified Machine Learning – Specialty
* Generative AI with Large Language Models
* LangChain for LLM Application Development

---

## ACHIEVEMENTS

* Delivered AI solutions reducing manual effort by 60%.
* Developed production-ready LLM applications serving thousands of users.
* Optimized LLM API costs through prompt engineering and retrieval optimization.
* Contributed to AI automation initiatives across multiple business domains.

---

## SOFT SKILLS

* Problem Solving
* Communication
* Team Collaboration
* Analytical Thinking
* Agile Development
* Stakeholder Management
"""
system_prompt = f"""You are a portfolio AI assistant 
Your task is to answer to the questions asked by a user based on the {resume},
REMEMBER: 
Only give response based on provided details from {resume}
Don't halluginate anything 
If the content that is asked by the user is not available in {resume} , then return "NO data available , sorry" """

user_prompt = input("Describe your requirement")
system_message = {
    "role": "system",
    "content": system_prompt
}
user_message = {
    "role": "user",
    "content": user_prompt
}
messages = [system_message, user_message]
response = client.chat.completions.create(model=model , temperature=0.7 , messages=messages)
answer = response.choices[0].message.content
print(answer)


















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































