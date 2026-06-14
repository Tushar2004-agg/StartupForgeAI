from agents.research_agent import model

def create_investor_plan(startup_name, industry):

    prompt = f"""
    Create an investor readiness report.

    Startup Name: {startup_name}
    Industry: {industry}

    Give:
    1. SWOT Analysis
    2. Funding Recommendation
    3. Investor Pitch Summary
    4. Risks
    5. Growth Potential
    """

    response = model.generate_content(prompt)

    return response.text