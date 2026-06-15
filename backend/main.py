from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from agents.chat_agent import chat_with_startup

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


class ReportData(BaseModel):
    report: str

class ChatRequest(BaseModel):
    report: str
    question: str


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


@app.post("/download-pdf")
def download_pdf(data: ReportData):

    pdf_file = "startup_report.pdf"

    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 780, "StartupForge AI Report")

    c.line(50, 770, 550, 770)

    y = 740

    headings = [
        "Executive Summary",
        "Market Opportunity",
        "Business Strategy",
        "Financial Outlook",
        "Marketing Roadmap",
        "Investment Readiness",
        "Final Recommendation"
    ]

    for line in data.report.split("\n"):

        line = line.strip()

        if not line:
            y -= 10
            continue

        if y < 60:
            c.showPage()
            y = 780

        is_heading = False

        for heading in headings:
            if heading.lower() in line.lower():

                c.setFont("Helvetica-Bold", 14)
                c.drawString(50, y, line)

                y -= 20

                is_heading = True
                break

        if not is_heading:
            c.setFont("Helvetica", 10)

            while len(line) > 90:

                c.drawString(50, y, line[:90])

                line = line[90:]

                y -= 15

                if y < 60:
                    c.showPage()
                    y = 780

            c.drawString(50, y, line)

            y -= 15

    c.save()

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename="startup_report.pdf"
    )