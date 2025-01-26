import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key = os.getenv('GEMINI_API_KEY'))

def generate_roadmap(subjects,hours,deadlines):
    prompt = f"""
    Create a study roadmap with:
    - Subjects: {subjects}
    - Study hours/day: {hours} hours
    - Deadlines: {deadlines}

    Rules:
    1. Allocate ALL {hours} hours every day.
    2. Spread topics until the deadline ({deadlines}), not just a few days.
    3. Include time for revision, exercises, and projects.
    4. Format as bullet points with Day X, Topics, Time, Priority.
    """
    model = genai.GenerativeModel ('gemini-pro')
    response =  model.generate_content(prompt)
    return response.text

if __name__ == '__main__':
    subjects = input("Subjects (comma separated): ").split(',')
    hours = int(input("how many hours you will study: "))
    deadlines = input("Deadlines (format 'Subject:YYYY-MM-DD ").split(',')

    roadmap = generate_roadmap(subjects,hours,deadlines)
    print("\n Your Study Roadmap: \n")
    print(roadmap)