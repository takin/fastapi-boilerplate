# FastAPI Boilerplate

A FastAPI based REST API project boilerplate. This to allow a fast project initialization

## 🚀 Features

- **FastAPI Framework**: High-performance, modern Python web framework
- **Python 3.13+**: Latest Python features and performance improvements
- **Async Support**: Built-in async/await support for high concurrency
- **Auto-generated Documentation**: Interactive API docs with Swagger UI and ReDoc
- **Environment Configuration**: Flexible configuration management with Pydantic Settings
- **Development Tools**: Pre-commit hooks, linting, and type checking
- **Redis Integration**: Ready for caching and session management
- **Database Ready**: PostgreSQL configuration included

## 📋 Prerequisites

- Python 3.13 or higher
- pip or uv package manager
- Redis (for caching and session management)
- PostgreSQL (for database operations)

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd tms
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -e .
   ```

   Or using uv (recommended):

   ```bash
   uv sync
   ```

4. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

## ⚙️ Configuration

Create a `.env` file in the root directory:

```env
# Environment
ENV=dev

# API Configuration
API_PORT=8000
API_HOST=localhost

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=postgres

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=redis
REDIS_DB=0

# Logging
LOG_LEVEL=info
```

## 🚀 Running the Application

### Development Mode

```bash
python main.py
```

The API will be available at:

- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📁 Project Structure

```
root/
├── app/                    # Application package
│   ├── __init__.py
│   ├── app.py            # FastAPI application factory
│   ├── api/              # API routes and endpoints
│   ├── models/           # Data models and schemas
│   └── services/         # Business logic and services
├── config/               # Configuration management
│   ├── __init__.py
│   └── app_config.py    # Application configuration
├── utils/                # Utility functions and helpers
├── main.py              # Application entry point
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Dependency lock file
└── README.md            # This file
```

## 🧪 Development

### Pre-commit Hooks

Install and run pre-commit hooks:

```bash
pre-commit install
pre-commit run --all-files
```

### Code Quality

- **Linting**: pylint for code quality checks
- **Type Checking**: pyright for static type analysis
- **Formatting**: black for code formatting (88 character line length)
- **Import Sorting**: isort for import organization

### Running Tests

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Run specific checks
pylint app/ config/ utils/
pyright
```

## 📚 API Documentation

Once the application is running, you can access:

- **Swagger UI**: http://localhost:8000/docs - Interactive API documentation
- **ReDoc**: http://localhost:8000/redoc - Alternative API documentation
- **OpenAPI Schema**: http://localhost:8000/openapi.json - Raw OpenAPI specification

## 🔧 Environment Variables

| Variable         | Default     | Description                      |
| ---------------- | ----------- | -------------------------------- |
| `ENV`            | `dev`       | Environment (dev, staging, prod) |
| `API_PORT`       | `8000`      | API server port                  |
| `API_HOST`       | `localhost` | API server host                  |
| `DB_HOST`        | `localhost` | PostgreSQL host                  |
| `DB_PORT`        | `5432`      | PostgreSQL port                  |
| `DB_USER`        | `postgres`  | PostgreSQL username              |
| `DB_PASSWORD`    | `postgres`  | PostgreSQL password              |
| `DB_NAME`        | `postgres`  | PostgreSQL database name         |
| `REDIS_HOST`     | `localhost` | Redis host                       |
| `REDIS_PORT`     | `6379`      | Redis port                       |
| `REDIS_PASSWORD` | `redis`     | Redis password                   |
| `REDIS_DB`       | `0`         | Redis database number            |
| `LOG_LEVEL`      | `info`      | Logging level                    |

## 🚀 Deployment

### Docker (Recommended)

```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY . .

RUN pip install -e .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment-specific Configurations

- **Development**: Uses `.env` file with local settings
- **Staging/Production**: Set environment variables directly or use configuration management systems

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:

- Create an issue in the repository
- Contact the development team
- Check the API documentation at `/docs`

---

**Built with ❤️ using FastAPI and Python 3.13+**
