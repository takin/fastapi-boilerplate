import logging

from contextlib import asynccontextmanager
from typing_extensions import AsyncGenerator
from fastapi import FastAPI

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    try:
        logger.info("Starting server...")
        yield
        logger.info("Shutdown server...")
    finally:
        logger.info("Server shutdown complete")

def init_app() -> FastAPI:

    app = FastAPI(
        title="AI Talent Management System API",
        description="The API service for talent management system with AI",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan
    )


    @app.get("/")
    def index():
        return {"message": "Hello, World!"}

    return app
