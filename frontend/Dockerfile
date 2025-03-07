# Use official Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies and build
RUN npm install && npm run build

# Install serve to serve static files
RUN npm install -g serve

# Expose port for frontend
EXPOSE 3000

# Start the app
CMD ["serve", "-s", "build", "-l", "3000"]
