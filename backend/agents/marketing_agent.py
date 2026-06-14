from agents.research_agent import model

def create_marketing_plan(startup_name, industry):

    prompt = f"""
    Create a marketing strategy for:

    Startup Name: {startup_name}
    Industry: {industry}

    Give:
    1. Instagram Strategy
    2. LinkedIn Strategy
    3. Launch Campaign
    4. Growth Strategy
    5. Customer Acquisition Plan
    """

    response = model.generate_content(prompt)

    return response.text