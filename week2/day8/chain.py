from groq import Groq
import os 
from dotenv import load_dotenv
load_dotenv()
model = "llama-3.3-70b-versatile"
my_key = os.getenv("GROQ_API_KEY")
if not my_key:
    raise ValueError("key not available")

client = Groq(api_key= my_key)

Job_description = f"""**AI Engineer – Startup**

We seek an AI Engineer with expertise in Python, Machine Learning, Deep Learning, NLP, TensorFlow/PyTorch, SQL, Git, and cloud platforms (AWS/GCP). Requirements: Bachelor's in CS or related field, experience with model deployment, APIs, MLOps, and strong problem-solving and communication skills.
"""
resume = f"""# **John Doe**

**Machine Learning Engineer**

**Email:** [john.doe@email.com](mailto:john.doe@email.com)
**Phone:** +1 234-567-8901
**LinkedIn:** linkedin.com/in/johndoe
**GitHub:** github.com/johndoe

## Professional Summary

Machine Learning Engineer with experience in building, training, and deploying scalable ML models. Proficient in developing AI-driven solutions using modern ML frameworks and cloud technologies.

## Technical Skills

* **Programming:** Python, SQL, Java
* **Machine Learning:** Supervised & Unsupervised Learning, Deep Learning, NLP, Computer Vision
* **Frameworks:** TensorFlow, PyTorch, Scikit-learn, Keras
* **Data Processing:** Pandas, NumPy, Spark
* **MLOps:** Docker, Kubernetes, MLflow, CI/CD
* **Cloud:** AWS, Google Cloud Platform (GCP), Azure
* **Databases:** MySQL, PostgreSQL, MongoDB
* **Tools:** Git, GitHub, Jupyter Notebook

## Education

**Bachelor of Technology in Computer Science**
XYZ University | 2022–2026

## Projects

### Customer Churn Prediction

* Built a classification model using XGBoost and Scikit-learn.
* Achieved 92% prediction accuracy through feature engineering and hyperparameter tuning.

### Image Classification

* Developed a CNN-based image classifier using TensorFlow.
* Improved model accuracy using data augmentation and transfer learning.

## Experience

**Machine Learning Intern** | ABC Technologies

* Developed predictive models for business analytics.
* Automated data preprocessing and model evaluation pipelines.
* Collaborated with software engineers to deploy ML models via REST APIs.

## Certifications

* Machine Learning Specialization
* Deep Learning Certification
* AWS Certified Cloud Practitioner

## Soft Skills

* Problem Solving
* Communication
* Team Collaboration
* Analytical Thinking
* Time Management
"""


def ask_llm(system_prompt , user_prompt):
    system_message = {
        "role": "system",
        "content":system_prompt
    }
    user_message = {
        "role": "user",
        "content":user_prompt
    }
    messages = [system_message, user_message]
    response = client.chat.completions.create(model=model , messages=messages)
    answer = response.choices[0].message.content
    return answer


def extract_jd(JD):
    system_prompt = f"""You are HR manager and task is to extract the all tecnical skills from the job discription
    Only extract the those defined in the {JD}
    Don't not generate by you own
    It should be comma seperated
    """
    user_prompt = f"""Extract from {Job_description}"""
    return ask_llm(system_prompt,user_prompt)

def extract_resume(resum):
    system_prompt = f"""You are HR manager and task is to extract the all technical skills from the resume
        Only extract the those defined in the {resum}
        Don't not generate by you own
        It should be comma seperated
        
        """
    user_prompt = f"""Extract from {resume}"""
    return ask_llm(system_prompt,user_prompt)

def score(jd , resume):
    system_prompt = f"""You are HR manager compare the technical skills of the {jd} and the {resume} 
        Score on the scale of 1-10 on basis of matching
        Don't use any skill which is not defined in {jd}
        """
    user_prompt = f"""compare the {jd} and {resume}"""
    return ask_llm(system_prompt,user_prompt)

job_skills = extract_jd(Job_description)
resume_skills = extract_resume(resume)
Final_score = score(job_skills,resume_skills)
print(Final_score)
