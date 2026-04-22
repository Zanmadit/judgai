from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LLAMA_ENDPOINT: str
    UPLOAD_DIR: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
