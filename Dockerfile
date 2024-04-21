# Use an official Python runtime as a parent image
FROM python:3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the assignment.py file into the container
COPY Assignment_Paragraphs.py paragraphs.txt /app

# Run the Python script when the container launches
CMD ["python", "Assignment_Paragraphs.py"]