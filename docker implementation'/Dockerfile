# Use the official Python image as a base
FROM python:3.10-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . /app

# Expose the port that your model will be served on (if applicable)
EXPOSE 5000

# Command to run the application (e.g., start a server, etc.)
CMD ["python", "SIMPLE NEURAL NET.py"]
