# Grocery App

## Setup Instructions

### 1. Backend (FastAPI)
- Create a virtual environment and install dependencies:
  ```sh
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
- Run the FastAPI server:
  ```sh
  uvicorn main:app --host 0.0.0.0 --port 8000
  ```

### 2. Frontend (React)
- Install dependencies and start the frontend:
  ```sh
  npm install
  npm start
  ```

### 3. Deployment on PythonAnywhere
- Follow the guide in `deploy/setup.sh`

