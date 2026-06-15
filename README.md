# 🚀 StartupForge AI

StartupForge AI is a Multi-Agent AI platform that helps entrepreneurs evaluate startup ideas, generate business plans, analyze financial viability, assess investment readiness, and receive AI-powered recommendations.

## 🌟 Features

* Multi-Agent Startup Analysis
* Research Agent
* Business Strategy Agent
* Finance Planning Agent
* Marketing Strategy Agent
* Investor Readiness Agent
* AI Startup Report Generation
* Knowledge-Enhanced Analysis (RAG Lite)
* PDF Report Download
* AI Startup Advisor Chat
* Interactive Dashboard
* FastAPI Backend
* Next.js Frontend
* LangGraph Workflow Orchestration
* Gemini AI Integration

---

## 🏗️ Architecture

```text
┌─────────────────────┐
│       User          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Next.js Frontend  │
│  (React + Tailwind) │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   FastAPI Backend   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     LangGraph       │
│ Workflow Orchestrator│
└──────────┬──────────┘
           │
 ┌─────────┼─────────┐
 │         │         │
 ▼         ▼         ▼
Research  Business  Finance
 Agent     Agent     Agent

 ▼         ▼         ▼
Marketing Investor  Report
 Agent     Agent    Agent

           │
           ▼
┌─────────────────────┐
│     Gemini AI       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Startup Report    │
└───────┬─────┬───────┘
        │     │
        ▼     ▼
    PDF Export
        │
        ▼
 AI Startup Chat

Knowledge Base (RAG Lite)
        │
        ▼
 startup_basics.txt
 marketing.txt
 funding.txt
```


---

## 🛠️ Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* Python
* LangGraph
* Google Gemini

### AI Components

* Multi-Agent Architecture
* Retrieval-Augmented Generation (RAG Lite)
* Prompt Engineering

### Deployment

* Vercel
* Render

---

## 🚀 Workflow

1. User enters startup details.
2. Multiple AI agents analyze the idea.
3. LangGraph coordinates the workflow.
4. Final startup report is generated.
5. User can download reports as PDF.
6. User can chat with the AI Startup Advisor.

---

## 📂 Project Structure

```text
StartupForgeAI
│
├── backend
│   ├── agents
│   ├── graph
│   ├── rag
│   ├── data
│   └── main.py
│
├── frontend
│   ├── src
│   ├── components
│   └── app
│
└── README.md
```

---

## 🌐 Deployment

### Frontend

Deployed on Vercel

### Backend

Deployed on Render

---

## 👨‍💻 Author

**Tushar Aggarwal**

B.Tech Computer Science Engineering

StartupForge AI – 2026
