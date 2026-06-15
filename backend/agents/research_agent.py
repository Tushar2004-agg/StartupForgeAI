import os
from dotenv import load_dotenv
import google.generativeai as genai
from rag.load_knowledge import load_knowledge

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_startup(startup_name, industry, budget, location):

    knowledge = load_knowledge()

    prompt = f"""
    You are a startup research expert.

    Use the following knowledge base while generating your analysis.

    Knowledge Base:
    {knowledge}

    Startup Details:

    Startup Name: {startup_name}
    Industry: {industry}
    Budget: {budget}
    Location: {location}

    Analyze the startup and provide:

    1. Market Opportunity
    2. Target Audience
    3. Top Competitors
    4. Revenue Model
    5. Risks
    6. Growth Strategy
    7. Final Recommendations

    Make the response professional, detailed and practical.
    """

    response = model.generate_content(prompt)

    return response.text