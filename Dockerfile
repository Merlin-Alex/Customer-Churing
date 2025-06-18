# 1. Base image
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy requirements first (to leverage Docker cache)
COPY requirements.txt .

# 4. Install system dependencies and Python packages
RUN apt-get update && apt-get install -y --no-install-recommends gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc && \
    rm -rf /var/lib/apt/lists/*

# 5. Copy the rest of the app code
COPY . .

# 6. Run FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
