# Use official Python image as base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y netcat gcc

# Copy requirements.txt and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files to the container
COPY . /app/

# Run Django collectstatic (optional for static files)
# RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
