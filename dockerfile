# Use an official Python runtime as a parent image
FROM python:3.10.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app directory contents into the container at /app
COPY ./app /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
CMD python main.py

EXPOSE 5000

# CMD python main.py
# Run app.py when the container launches
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
