# Use a base image (example: Python)
FROM python:3.9
# Set working directory
WORKDIR /app
# Copy application files to the container
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire app directory to the container
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the application
CMD ["python3", "app.py"]

