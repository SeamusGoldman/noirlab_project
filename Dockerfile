# Use a slim Python image for a smaller container size
FROM python:3.12-slim

# Set environment variables
ENV PYTHONPATH=/code/src
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /code

# Install system dependencies needed for PostgreSQL and Python compilation
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy the application source code into the container
COPY src /code/src
COPY pyproject.toml pdm.lock alembic.ini /code/
COPY migrations /code/migrations

# Install PDM and project dependencies
RUN pip install --no-cache-dir pdm && pdm sync --dev

# Expose the FastAPI default port
EXPOSE 8000

# Run Alembic migrations before starting FastAPI
CMD ["sh", "-c", "cd /code && pdm run alembic upgrade head && pdm run uvicorn app.api.run_app:app --host 0.0.0.0 --port 8000 --reload"]
