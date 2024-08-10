# Use an official Python runtime as a parent image
# Set the working directory in the container
# Copy the current directory contents into the container at /app
# Install any needed packages specified in requirements.txt
# Copy the Scores.txt file into the container
# Make port 5000 available to the world outside this container
# Define environment variable
# Run app.py when the container launches

FROM python:3.9-slim


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


COPY Scores.txt /Scores.txt


EXPOSE 5000


ENV NAME=World


CMD ["python", "main_score.py"]
