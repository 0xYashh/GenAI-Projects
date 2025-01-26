import os
import google.generativeai as genai
from dotenv import load_dotenv
from rich.console import Console

console = Console()
load_dotenv()
genai.configure(api_key = os.getenv('GEMINI_API_KEY'))

def generate_roadmap(user_prompt):
    system_prompt = f"""
You are an expert study planner. Create a daily roadmap based on this request:
"{user_prompt}"

**Strict Rules:**
1. Time Allocation:
   - Fully utilize all specified daily hours/day)
   - Split time between theory (40%), practice (40%), and revision (20%)

2. Content Structure:
   - Follow logical progression: Foundations → Core Concepts → Advanced Topics
   - Ensure all mentioned subjects/topics are covered
   - Include concrete exercises/projects for practical application

3. Format Requirements:
   - Plain text format (NO markdown/bold/formatting)
   - Use this exact structure:
     Day [X]:
     - [Topic]: [Time Allocation] (Theory/Practice/Revision)
     - [Topic]: [Time Allocation] (Practice)
     - [Activity]: [Time Allocation] (Exercise/Project)

4. Special Considerations:
   - Account for specified deadlines in date calculations
   - Include spaced repetition for better retention
   - Add progress checkpoints every 3 days
"""
    model = genai.GenerativeModel ('gemini-pro')
    response =  model.generate_content(user_prompt)
    return response.text

if __name__ == '__main__':
    user_input = console.input("[bold green]Enter your goal (e.g., 'I want to learn ML in 10 days, 5 hours/day'): [/]")
    
    roadmap = generate_roadmap(user_input)
    console.print("\n[bold cyan]Your Personalized Roadmap:[/]\n")
    console.print(roadmap)