from fastapi import APIRouter, HTTPException

from app.models import SQLRequest, SQLResponse
from app.prompt import build_prompt
from app.groq_service import groq_service

router = APIRouter(
    prefix="/api/v1",
    tags=["AI SQL Generator"]
)


@router.post(
    "/generate-sql",
    response_model=SQLResponse,
    summary="Generate SQL from Natural Language",
)
async def generate_sql(request: SQLRequest):
    """
    Convert a natural language question into an SQL query.
    """

    try:
        # Build the prompt
        prompt = build_prompt(request.question)

        # Generate SQL using Groq
        sql = groq_service.generate_sql(prompt)

        # Return response
        return SQLResponse(
            question=request.question,
            sql=sql
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )