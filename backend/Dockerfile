# Use official Python image
FROM python:3.9-slim AS backend

# Set working directory
WORKDIR /app

# Copy backend requirements and install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

# Ensure Uvicorn is installed
RUN pip install uvicorn 

# Expose port 80
EXPOSE 80

# Run FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
