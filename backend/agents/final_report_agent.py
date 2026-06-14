from agents.research_agent import model

def generate_final_report(
    startup_name,
    research,
    business,
    finance,
    marketing,
    investor
):

    prompt = f"""
    Create a professional startup report.

    Startup Name:
    {startup_name}

    Research Analysis:
    {research}

    Business Analysis:
    {business}

    Finance Analysis:
    {finance}

    Marketing Analysis:
    {marketing}

    Investor Analysis:
    {investor}

    Generate:

    1. Executive Summary
    2. Market Opportunity
    3. Business Strategy
    4. Financial Outlook
    5. Marketing Roadmap
    6. Investment Readiness
    7. Final Recommendation
    """

    response = model.generate_content(prompt)

    return response.text