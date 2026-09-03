# 📈 Autonomous Multi-Agent BI Copilot

An enterprise-ready Business Intelligence application powered by autonomous AI agents. The platform ingests business prompts and CSV datasets to generate structured executive decision reports.

## 🚀 Key Features

- **Sequential Multi-Agent Pipeline:** Coordinates a Data Analyst Agent and a Strategy Advisor Agent to perform root-cause analysis and strategic planning.
- **Dynamic CSV Data Ingestion:** Reads structured spreadsheet data (`.csv`) and feeds relevant column contexts directly into agent context windows.
- **High-Speed Inference:** Powered by Groq Llama 3 70B for fast sequential execution.
- **Interactive Web Interface:** Streamlit UI for seamless prompt entry, dataset previewing, and markdown report rendering.
- **One-Click Export:** Download final executive reports directly as `.md` files.

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **Agent Orchestration:** CrewAI
- **LLM Provider:** Groq API (Llama-3.3-70b-versatile)
- **Frontend:** Streamlit
- **Data Handling:** Pandas

## 📦 Installation & Local Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/bi-copilot.git](https://github.com/YOUR_USERNAME/bi-copilot.git)
   cd bi-copilot