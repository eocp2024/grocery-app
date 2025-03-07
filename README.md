# Grocery Shopping & Meal Planner App

This project is a Grocery Shopping & Meal Planner App that consists of a FastAPI backend and a React frontend. 

## How to Run
1. **Backend**:
   ```bash
   pip install -r backend/requirements.txt
   uvicorn main:app --reload
   ```

2. **Frontend**:
   ```bash
   npm install
   npm start
   ```

## Deployment
### Using Docker:
1. Build and Run:
   ```bash
   docker build -t grocery-app -f deploy/Dockerfile .
   docker run -p 80:80 grocery-app
   ```

### Using Railway:
1. Push the project to GitHub and connect it to Railway.
2. Railway will deploy automatically using `railway.json`.

## License
This project is licensed under the MIT License.
