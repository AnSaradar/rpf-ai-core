# Reparameterized Foundation – AI Assistant for the Syrian Post-Crisis Platform
# RPF AI CORE

This project is an AI-powered assistant developed for the **Reparameterized Foundation**. It supports the **Syrian Post-Crisis Platform**, a centralized hub that aids in data collection, visualization, and statistical reporting for rebuilding Syria.

## 💡 Project Overview

The platform is designed to:

- Act as a **data center** for various stakeholders interested in Syria's recovery.
- Provide **statistical insights**, **infrastructure reports**, and other relevant data.
- Enable users to **ask questions** and generate **summaries or reports** through an intelligent chat interface powered by AI.

Whether you're a researcher, policymaker, NGO worker, or simply someone seeking accurate data about Syria, this platform is built to help.

---

## 🚀 Features

- AI-powered Q&A interface for Syrian data.
- On-demand summary and report generation.
- Scalable and modular backend with FastAPI.
- Foundation for future data integrations and analytics tools.

---

## 🛠 Tech Stack

- **Python 3.11**
- **FastAPI**
- **Pydantic**
- AI/LLM components (e.g., OpenAI, LangChain, etc. — if used, to be updated)
- MongoDB or any other DB (to be mentioned if integrated)

---

## 🧪 Setup & Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## 📁 Project Structure

```
├── assets/        # Temporary storage for uploaded files
├── controllers/   # Core business logic, organized by features such as file validation, text extraction, and chunking
├── core/          # Configuration, dependency setup, and utility methods
├── dtos/          # Request and Response schemas for each API endpoint
├── llm/           # Logic for handling LLM scripts and provider integrations
├── routes/        # API route definitions
├── schemas/       # MongoDB entity schemas
├── services/      # CRUD operations for MongoDB entities
├── vectordb/      # Vector database provider integration and management
```

Each folder in the project follows a specific responsibility, ensuring a clean separation of concerns and maintainability.
