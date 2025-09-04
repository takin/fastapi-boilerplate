"""
AI Talent Management System API

The API service for talent management system with AI
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from typing_extensions import AsyncGenerator

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """The lifespan of the app"""
    try:
        logger.info("Starting server...")
        yield
        logger.info("Shutdown server...")
    finally:
        logger.info("Server shutdown complete")


def init_app() -> FastAPI:
    """The initialization of the app"""
    app = FastAPI(
        title="AI Talent Management System API",
        description="The API service for talent management system with AI",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    @app.get("/")
    def index():
        return {"message": "Hello, World!"}

    return app
