from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="AI SQL Assistant",
    description="""
AI SQL Assistant converts natural language into SQL queries using the Groq API.

Features:
- Natural Language → SQL
- Fake Database Schema
- No Real Database Required
- FastAPI + Groq
""",
    version="1.0.0",
)

# Include all API routes
app.include_router(router)


@app.get("/", tags=["Home"])
async def home():
    """
    Home endpoint.
    """
    return {
        "message": "Welcome to AI SQL Assistant",
        "status": "Running"
    }


@app.get("/health", tags=["Health"])
async def health():
    """
    Health check endpoint.
    """
    return {
        "status": "OK"
    }