from pydantic_settings import BaseSettings
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    MONGO_URI: str
    DB_NAME: str

    class Config:
        env_file = BASE_DIR / f".env.{os.getenv('ENV', 'development')}"
        if os.getenv('ENV') == 'test':
            env_file = BASE_DIR / '.env.test'
        env_file_encoding = "utf-8"

settings = Settings()
