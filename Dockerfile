# Use official Python base image
FROM python:3.12-slim

# Set Working directory for container
WORKDIR /CLI_Astro_Forecast

# Copying requirements.txt from root
COPY requirements.txt .

# Install dependencies for requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into container
COPY app/ .

# Define runtime environment variable
ENV DEBUG=0

# Run main.py on container startup
CMD ["python", "./main.py"]
