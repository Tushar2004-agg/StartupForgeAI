import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_startup(startup_name, industry, budget, location):

    prompt = f"""
    Analyze this startup idea:

    Startup Name: {startup_name}
    Industry: {industry}
    Budget: {budget}
    Location: {location}

    Give:
    1. Market Opportunity
    2. Target Audience
    3. Top Competitors
    4. Revenue Model
    5. Risks
    """

    response = model.generate_content(prompt)

    return response.text