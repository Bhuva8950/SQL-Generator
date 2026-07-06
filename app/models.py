from pydantic import BaseModel, Field


class SQLRequest(BaseModel):
    """
    Request model for SQL generation.
    """

    question: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Natural language question to convert into SQL.",
        examples=["Show all products with discount greater than 20%"]
    )


class SQLResponse(BaseModel):
    """
    Response model returned by the API.
    """

    question: str
    sql: str


class ErrorResponse(BaseModel):
    """
    Standard error response.
    """

    error: str