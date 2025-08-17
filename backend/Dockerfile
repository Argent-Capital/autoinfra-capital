FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app

# Render sets PORT env var; default to 8000 for local use
ENV PORT=8000
EXPOSE 8000

# Use shell form so ${PORT} expands at runtime
CMD sh -c "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"
