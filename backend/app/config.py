import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# This is a test comment for PR_TEST_2 branch in config.py.

class Config:
    PROJECT_NAME: str = "Vibe Coding W2-1 Backend"
    PROJECT_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"

    # LangChain/LangSmith configuration
    LANGCHAIN_TRACING_V2: str = os.getenv("LANGCHAIN_TRACING_V2", "false")
    LANGCHAIN_ENDPOINT: str = os.getenv("LANGCHAIN_ENDPOINT", "")
    LANGCHAIN_API_KEY: str = os.getenv("LANGCHAIN_API_KEY", "")
    LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT", "")

    # Google Gemini configuration
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")

config = Config()

class Settings:
    """애플리케이션 설정"""
    
    # 서버 설정
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # 개발/운영 환경
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"


settings = Settings() 