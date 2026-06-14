from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.research_agent import analyze_startup
from agents.business_agent import create_business_plan
from agents.finance_agent import create_finance_plan
from graph.startup_graph import graph

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StartupIdea(BaseModel):
    startup_name: str
    industry: str
    budget: str
    location: str

@app.get("/")
def home():
    return {
        "message": "StartupForge AI is running successfully"
    }

@app.post("/startup")
def create_startup_plan(data: StartupIdea):

    result = graph.invoke({
        "startup_name": data.startup_name,
        "industry": data.industry,
        "budget": data.budget,
        "location": data.location,
        "research": "",
        "business": "",
        "finance": "",
        "marketing": "",
        "investor": "",
        "final_report": ""
    })

    return {
    "startup_name": data.startup_name,
    "industry": data.industry,
    "location": data.location,
    "final_report": result["final_report"]
}