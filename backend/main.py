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

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 780, "StartupForge AI Report")

    c.setFont("Helvetica", 10)

    y = 740

    for line in data.report.split("\n"):

        if y < 50:
            c.showPage()
            y = 780
            c.setFont("Helvetica", 10)

        c.drawString(50, y, line[:100])
        y -= 15

    c.save()

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename="startup_report.pdf"
    )

@app.post("/chat")
def chat(data: ChatRequest):

    answer = chat_with_startup(
        data.report,
        data.question
    )

    return {
        "answer": answer
    }