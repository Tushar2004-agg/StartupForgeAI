from agents.research_agent import model

def create_business_plan(startup_name, industry):

    prompt = f"""
    Create a business plan for:

    Startup Name: {startup_name}
    Industry: {industry}

    Give:
    1. Business Model
    2. Customer Segments
    3. Value Proposition
    4. Revenue Streams
    """

    response = model.generate_content(prompt)

    return response.text