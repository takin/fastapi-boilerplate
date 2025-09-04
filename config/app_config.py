from pydantic_settings import BaseSettings
from pydantic import Field


class AppConfig(BaseSettings):

    api_port: int = Field(default=8000)
    api_host: str = Field(default="localhost")


    log_level: str = Field(default="info")


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

config = AppConfig()
