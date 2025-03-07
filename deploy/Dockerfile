# Backend
FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# Frontend
FROM node:14 as frontend

WORKDIR /app/frontend

COPY frontend/package.json .
RUN npm install

COPY frontend/ .

RUN npm run build

# Final Stage
FROM nginx:alpine

COPY --from=frontend /app/frontend/build /usr/share/nginx/html
COPY --from=0 /app /backend

EXPOSE 80
