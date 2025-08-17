# backend/Dockerfile
FROM python:3.11-slim

# Prevents Python from writing .pyc files & enables unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system deps (optional but helpful for psycopg2, reportlab fonts)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Copy deps & install
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app code
COPY app /app/app

# Render provides $PORT at runtime; default to 8000 for local use
ENV PORT=8000
EXPOSE 8000

# Start FastAPI with Uvicorn, using Render's $PORT
CMD sh -c "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"
