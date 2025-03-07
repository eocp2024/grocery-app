# Use an official Python image with pip installed
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (to optimize Docker caching)
COPY backend/requirements.txt .

# Install pip & dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend files
COPY backend/ .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
