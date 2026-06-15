from agents.research_agent import model

def chat_with_startup(report, question):

    prompt = f"""
    You are an AI Startup Advisor.

    Startup Report:

    {report}

    User Question:

    {question}

    Answer the question using the startup report context.
    Give practical and professional advice.
    """

    response = model.generate_content(prompt)

    return response.text