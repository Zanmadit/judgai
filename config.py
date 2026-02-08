from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    UPLOAD_DIR: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
