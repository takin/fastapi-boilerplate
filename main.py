import uvicorn
import logging

from dotenv import load_dotenv
from app import init_app
from config import config

logger = logging.getLogger(__name__)

load_dotenv()

app = init_app()

def main():
    try:
        uvicorn.run(
            "main:app",
            host=config.api_host,
            port=config.api_port,
            reload=True
        )
    except KeyboardInterrupt as e:
        logger.info("KeyboardInterrupt", e)


if __name__ == "__main__":
    main()
