from groq import Groq
import os
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not  api_key:
    raise ValueError("key not available...")
client = Groq(api_key= api_key)
model = "llama-3.3-70b-versatile"
job_description="""
Description
Do you want to solve real customer problems through innovative technology? Do you enjoy working on scalable services in a collaborative team environment? Do you want to see your code directly impact millions of customers worldwide?

At Amazon, we hire the best minds in technology to innovate and build on behalf of our customers. Customer obsession is part of our company DNA, which has made us one of the world's most beloved brands.

Our Software Development Engineers (SDEs) use modern technology to solve complex problems while seeing their work's impact first-hand. The challenges SDEs solve at Amazon are meaningful and influence millions of customers, sellers, and products globally. We seek individuals passionate about creating new products, features, and services while managing ambiguity in an environment where development cycles are measured in weeks, not years.

At Amazon, we believe in ownership at every level. As an SDE-I, you'll own the entire lifecycle of your code - from design through deployment and ongoing operations. This ownership mindset, combined with our commitment to operational excellence, ensures we deliver the highest quality solutions for our customers.

We're looking for curious minds who think big and want to define tomorrow's technology. At Amazon, you'll grow into the high-impact engineer you know you can be, supported by a culture of learning and mentorship. Every day brings exciting new challenges and opportunities for personal growth.
Key job responsibilities
• Collaborate and communicate effectively with experienced cross-disciplinary Amazonians to design, build, and operate innovative products and services that delight our customers, while participating in technical discussions to drive solutions forward.
• Design and develop scalable solutions using cloud-native architectures and microservices in a large distributed computing environment.
• Participate in code reviews and contribute to technical documentation.
• Build and maintain resilient distributed systems that are scalable, fault-tolerant, and cost-effective.
• Leverage and contribute to the development of GenAI and AI-powered tools to enhance development productivity while staying current with emerging technologies.
• Write clean, maintainable code following best practices and design patterns.
• Work in an agile environment practicing CI/CD principles while participating in operational responsibilities including on-call duties.
• Demonstrate operational excellence through monitoring, troubleshooting, and resolving production issues.
Basic Qualifications
- Experience with at least one general-purpose programming language such as Java, Python, C++, C#, Go, Rust, or TypeScript
- Experience with data structure implementation, basic algorithm development, and/or object-oriented design principles
- Currently has, or is in the process of obtaining a bachelor’s degree in Computer Science, Computer Engineering, Data Science, Information Systems, or related STEM fields
- Must be 18 years of age of older
Preferred Qualifications
- Experience from previous technical internship(s) or demonstrated project experience
- Experience with one or more of the following: AI tools for development productivity, Cloud platforms (preferably AWS), Database systems (SQL and NoSQL), Contributing to open-source projects, Version control systems, Debugging and troubleshooting complex systems
- Demonstrated ability to learn and adapt to new technologies quickly
- Basic understanding of software development lifecycle (SDLC)
- Strong problem-solving and analytical skills
- Excellent written and verbal communication skills
"""
class JobD(BaseModel):
    role : str
    required_skills : list[str]
    preferred_skills : list[str]
    min_exp          : float|None 
    educational_requirements : list[str]
    responsibilities : list[str]

jobd_schema = JobD.model_json_schema()

system_prompt = f"""
You are an expert HR assistant.

Your job is to analyze job descriptions and extract
structured information from them.

Return ONLY valid JSON matching this schema:

{jobd_schema}
IMPORTANT:
Do NOT return the schema itself.
Do NOT return fields like "properties", "title" or "type".
Fill the schema with actual information extracted from the job description.

If minimum experience is not mentioned, return null.
If information for a list is missing, return an empty list.
Do not invent information.
"""
user_prompt = f"""
Analyze the following job description: # Job Description: Senior AI Engineer

## Job Title

**Senior AI Engineer**

## Location

[Remote / Hybrid / On-site]

## Employment Type

Full-time

## About the Role

We are seeking a highly skilled and experienced Senior AI Engineer to lead the design, development, and deployment of cutting-edge artificial intelligence solutions. In this role, you will work closely with cross-functional teams to build scalable AI systems, production-grade machine learning models, and generative AI applications that solve complex business challenges. You will play a key role in shaping AI strategy, mentoring engineers, and driving innovation across the organization.

## Key Responsibilities

* Design, develop, and deploy production-ready AI, machine learning, and generative AI solutions.
* Build and optimize Large Language Model (LLM) applications using techniques such as Retrieval-Augmented Generation (RAG), prompt engineering, tool calling, and AI agents.
* Develop scalable ML pipelines for data ingestion, feature engineering, model training, evaluation, deployment, and monitoring.
* Fine-tune and evaluate foundation models using modern frameworks and best practices.
* Collaborate with product managers, software engineers, data scientists, and stakeholders to translate business requirements into AI-driven solutions.
* Architect cloud-native AI platforms leveraging services from AWS, Azure, or Google Cloud.
* Implement MLOps practices including CI/CD, model versioning, experiment tracking, monitoring, and automated retraining.
* Optimize AI systems for performance, latency, scalability, reliability, and cost efficiency.
* Establish AI governance standards, including model evaluation, explainability, fairness, privacy, and security.
* Mentor junior engineers and conduct technical design reviews and code reviews.
* Stay current with emerging AI technologies, research, and industry best practices.

## Required Qualifications

* Bachelor's or Master's degree in Computer Science, Artificial Intelligence, Machine Learning, Data Science, or a related field.
* 7+ years of software engineering experience with at least 4+ years focused on AI/ML development.
* Strong proficiency in Python and software engineering best practices.
* Experience with deep learning frameworks such as PyTorch or TensorFlow.
* Hands-on experience with LLMs and generative AI technologies including OpenAI, Anthropic, Gemini, or open-source models (Llama, Mistral, Qwen, etc.).
* Experience building AI applications using frameworks such as LangChain, LangGraph, LlamaIndex, AutoGen, CrewAI, or Semantic Kernel.
* Strong understanding of RAG architectures, vector databases, embeddings, and semantic search.
* Experience with vector databases such as Pinecone, Weaviate, Milvus, Chroma, or FAISS.
* Experience deploying AI applications using Docker, Kubernetes, and cloud platforms (AWS, Azure, or GCP).
* Knowledge of REST APIs, microservices, and distributed systems.
* Experience with SQL and NoSQL databases.
* Familiarity with Git, CI/CD pipelines, and Agile development methodologies.

## Preferred Qualifications

* Experience fine-tuning LLMs using LoRA, QLoRA, or parameter-efficient fine-tuning (PEFT).
* Experience with AI agents, multi-agent systems, and workflow orchestration.
* Knowledge of multimodal AI, computer vision, speech AI, or recommendation systems.
* Experience with GPU optimization, distributed training, or inference optimization.
* Familiarity with model monitoring, evaluation frameworks, and AI observability tools.
* Experience with data engineering tools such as Spark, Kafka, or Airflow.
* Contributions to open-source AI projects or published AI research are a plus.

## Technical Skills

### Programming

* Python
* SQL
* JavaScript/TypeScript (preferred)

### AI/ML

* Machine Learning
* Deep Learning
* NLP
* LLMs
* RAG
* Prompt Engineering
* AI Agents
* Fine-tuning
* Embeddings
* Vector Search

### Frameworks

* PyTorch
* TensorFlow
* LangChain
* LangGraph
* LlamaIndex
* Semantic Kernel
* MLflow

### Cloud & DevOps

* AWS / Azure / GCP
* Docker
* Kubernetes
* Terraform
* GitHub Actions / Azure DevOps / Jenkins

### Databases

* PostgreSQL
* MongoDB
* Redis
* Pinecone
* Weaviate
* FAISS
* Chroma

## Soft Skills

* Strong analytical and problem-solving abilities.
* Excellent communication and stakeholder management skills.
* Leadership and mentoring experience.
* Ability to drive technical strategy and architecture decisions.
* Strong collaboration across engineering, product, and business teams.
* Passion for innovation and continuous learning.

## Success Metrics

* Deliver scalable, production-grade AI solutions on time.
* Improve model performance, reliability, and operational efficiency.
* Reduce deployment time through robust MLOps practices.
* Drive AI adoption across business functions.
* Mentor engineers and foster engineering excellence.

## What We Offer

* Competitive compensation and performance-based incentives.
* Flexible work environment (remote/hybrid).
* Professional development and learning opportunities.
* Access to cutting-edge AI technologies and cloud infrastructure.
* Collaborative, innovation-driven engineering culture.
* Comprehensive health and wellness benefits.

"""

user_message = {
    'role': 'user',
    'content' : user_prompt
}

system_message = {
    'role': 'system',
    'content' : system_prompt
}

response_format = {
    'type' : 'json_object'
}
messages = [system_message , user_message]
response = client.chat.completions.create(model = model, temperature = 0, messages = messages , response_format = response_format)
answer = response.choices[0].message.content
raw_json = answer
import json
job_data = json.loads(raw_json)
job = JobD(**job_data)

