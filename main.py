"""
The entry point of an app
"""

import logging

import uvicorn
from dotenv import load_dotenv

from app import init_app
from config import config

logger = logging.getLogger(__name__)

load_dotenv()

app = init_app()


def main():
    """The entry point of an app"""
    try:
        uvicorn.run("main:app", host=config.api_host, port=config.api_port, reload=True)
    except KeyboardInterrupt as e:
        logger.info("KeyboardInterrupt: %s", e)


if __name__ == "__main__":
    main()
