from agents.research_agent import model

def create_finance_plan(startup_name, budget):

    prompt = f"""
    Startup: {startup_name}
    Budget: {budget}

    Give:
    1. Initial Cost Breakdown
    2. Monthly Expenses
    3. Revenue Forecast
    4. Break Even Estimate
    """

    response = model.generate_content(prompt)

    return response.text