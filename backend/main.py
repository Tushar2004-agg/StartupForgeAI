from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from reportlab.pdfgen import canvas

from agents.research_agent import analyze_startup
from agents.business_agent import create_business_plan
from agents.finance_agent import create_finance_plan
from graph.startup_graph import graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
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


@app.get("/download-pdf")
def download_pdf():

    pdf_file = "startup_report.pdf"

    c = canvas.Canvas(pdf_file)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 800, "StartupForge AI Report")

    c.setFont("Helvetica", 12)
    c.drawString(100, 760, "PDF download feature integrated successfully!")

    c.save()

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename="startup_report.pdf"
    )