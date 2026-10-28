# Use minimal official base image
FROM python:3.11-slim

# Set environment variables to prevent bytecode and buffer issues
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-root system user for security compliance
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Leverage Docker cache layers for dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and transfer ownership to the unprivileged user
COPY app.py .
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 5000

# Healthcheck to validate container status
HEALTHCHECK --interval=30s --timeout=3s CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/healthz')" || exit 1

CMD ["python", "app.py"]