# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY app.py .

# Install dependencies
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]


