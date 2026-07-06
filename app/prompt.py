from app.schema import DATABASE_SCHEMA


def build_prompt(user_question: str) -> str:
    """
    Builds the prompt that will be sent to the Groq model.

    Parameters:
        user_question (str): Natural language question from the user.

    Returns:
        str: Complete prompt for SQL generation.
    """

    prompt = f"""
You are an expert SQL developer.

Your task is to convert natural language into SQL queries.

===========================
DATABASE SCHEMA
===========================

{DATABASE_SCHEMA}

===========================
RULES
===========================

1. Generate ONLY SQL.
2. Do NOT explain anything.
3. Do NOT use Markdown.
4. Do NOT wrap SQL inside ``` blocks.
5. Use only the tables and columns provided.
6. Never invent table names.
7. Never invent column names.
8. If the question cannot be answered using the schema,
   return:

INVALID_QUERY

9. Assume SQLite syntax.
10. Generate clean, readable SQL.

===========================
USER QUESTION
===========================

{user_question}

===========================
SQL
===========================
"""

    return prompt.strip()