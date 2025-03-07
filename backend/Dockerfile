# Use an official Python image as the base
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip

# Upgrade pip
RUN pip install --upgrade pip

# Copy and install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Explicitly install Uvicorn
RUN pip install uvicorn

# Copy the rest of the application
COPY backend/ .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Start the FastAPI server
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
