# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app/backend
COPY backend/requirements.txt /app/backend/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy the entire project into the container at /app
COPY . /app

# Change the working directory to /app/backend
WORKDIR /app/backend

# Expose the port that the app will run on
EXPOSE 8000

# Define the command to run your app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
