# Use a slim Python image for smaller container size
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml pdm.lock /app/

RUN pip install --no-cache-dir pdm

RUN pdm sync

COPY . /app

EXPOSE 8000

CMD ["celestial-app"]
