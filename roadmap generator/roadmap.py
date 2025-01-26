import os
import google.generativeai as genai
from dotenv import load_dotenv
from rich.console import Console

console = Console()
load_dotenv()
genai.configure(api_key = os.getenv('GEMINI_API_KEY'))
def clean_response(text):
    return text.replace('**','').replace("*","").strip()
def generate_roadmap(user_prompt):
    system_prompt = f"""
You are an expert study planner. Create a daily roadmap based on:
"{user_prompt}"

**Strict Rules:**
1. Format:  
   - **PLAIN TEXT ONLY**. NEVER use markdown, bold, asterisks, or special formatting. YOU CAN USE POINTS (e.g., hyphens).
   - Structure:  
     Day [X] ([Total Hours] hours):  
     - [Topic]: [Time] (Theory/Practice/Revision)  
     - [Activity]: [Time] (Exercise/Project)  

2. Content:  
   - Allocate ALL hours specified per day.  
   - Split time: Theory (40%), Practice (40%), Revision (20%).  
   - Example of Project Ideas: "Build a spam email classifier".
   - Order: Basics → Intermediate → Advanced.  

3. Example Output:  
   Day 1 (5 hours):  
   - 1.thon Basics: 2 hours (Theory)  
   - 2.riables Practice: 2 hours (Practice)  
   - 3.de Exercises: 1 hour (Exercise)  
   - 4.oject Idea : "Build a calculaur"
   - 5.oject Idea : " Build a house predicting linear regression model".
4 **Resources**:
   - Add a "Resources" section at the end with:
     - YouTube channels (e.g., "StatQuest for ML concepts")[Links].
     - Books (e.g., "Hands-On Machine Learning by Aurélien Géron")[Links].
     - Tools (e.g., "Jupyter Notebook, Scikit-learn")[Links].
   - Ensure resources are relevant and beginner-friendly.

5 **Creativity**:
   - Add engaging activities (e.g., "Build a spam email classifier").
   - Include practical projects (e.g., "Predict house prices using regression").
   - Suggest real-world datasets (e.g., "Titanic dataset for classification").

**Important:**  
- **NEVER** use **bold**, *italics*, `code blocks`, or markdown.  
- Use hyphens (`-`) for lists, colons (`:`) for time allocation.  
- Strictly follow the example format above.  
"""
    model = genai.GenerativeModel ('gemini-pro')
    response =  model.generate_content(user_prompt)
    return clean_response( response.text )

if __name__ == '__main__':
    user_input = console.input("[bold green]Enter your goal (e.g., 'I want to learn ML in 10 days, 5 hours/day'): [/]")
    
    roadmap = generate_roadmap(user_input)
    console.print("\n[bold cyan]Your Personalized Roadmap:[/]\n")
    console.print(roadmap)