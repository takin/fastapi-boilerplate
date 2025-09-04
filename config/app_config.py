"""
The main configuration class for the entire app
"""

from pydantic import Field
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """The main configuration class for the entire app"""

    env: str = Field(default="dev")

    # API configuration
    api_port: int = Field(default=8000)
    api_host: str = Field(default="localhost")

    log_level: str = Field(default="info")

    # Database configuration
    db_host: str = Field(default="localhost")
    db_port: int = Field(default=5432)
    db_user: str = Field(default="postgres")
    db_password: str = Field(default="postgres")
    db_name: str = Field(default="postgres")

    # Redis configuration
    redis_host: str = Field(default="localhost")
    redis_port: int = Field(default=6379)
    redis_password: str = Field(default="redis")
    redis_db: int = Field(default=0)

    class Config:
        """The configuration class for the app"""

        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"


config = AppConfig()
