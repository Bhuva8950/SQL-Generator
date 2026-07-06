from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()


class Settings:
    """
    Application configuration.

    All environment variables are loaded once and can be
    accessed throughout the application using the
    settings object.
    """

    # Groq API Key
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # LLM Configuration
    MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 512))


# Global settings instance
settings = Settings()