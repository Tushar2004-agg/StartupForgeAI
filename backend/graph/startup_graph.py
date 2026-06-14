from typing import TypedDict
from agents.research_agent import analyze_startup
from agents.business_agent import create_business_plan
from agents.finance_agent import create_finance_plan
from langgraph.graph import StateGraph, END
from agents.marketing_agent import create_marketing_plan
from agents.investor_agent import create_investor_plan
from agents.final_report_agent import generate_final_report

class StartupState(TypedDict):
    startup_name: str
    industry: str
    budget: str
    location: str

    research: str
    business: str
    finance: str
    marketing: str
    investor: str   
    final_report: str

def research_node(state: StartupState):

    result = analyze_startup(
        state["startup_name"],
        state["industry"],
        state["budget"],
        state["location"]
    )

    state["research"] = result

    return state



def business_node(state: StartupState):

    result = create_business_plan(
        state["startup_name"],
        state["industry"]
    )

    state["business"] = result

    return state



def finance_node(state: StartupState):

    result = create_finance_plan(
        state["startup_name"],
        state["budget"]
    )

    state["finance"] = result

    return state

def final_report_node(state: StartupState):

    state["final_report"] = generate_final_report(
        state["startup_name"],
        state["research"],
        state["business"],
        state["finance"],
        state["marketing"],
        state["investor"]
    )

    return state

def marketing_node(state: StartupState):

    state["marketing"] = create_marketing_plan(
        state["startup_name"],
        state["industry"]
    )

    return state

def investor_node(state: StartupState):

    state["investor"] = create_investor_plan(
        state["startup_name"],
        state["industry"]
    )

    return state



builder = StateGraph(StartupState)

builder.add_node("research", research_node)
builder.add_node("business", business_node)
builder.add_node("finance", finance_node)
builder.add_node("marketing", marketing_node)
builder.add_node("investor", investor_node)
builder.add_node("final_report", final_report_node)

builder.set_entry_point("research")

builder.add_edge("research", "business")
builder.add_edge("business", "finance")
builder.add_edge("finance", "marketing")
builder.add_edge("marketing", "investor")
builder.add_edge("investor", "final_report")
builder.add_edge("final_report", END)

graph = builder.compile()
