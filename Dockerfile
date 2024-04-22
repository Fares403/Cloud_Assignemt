# Use the official Python slim image as a base image
FROM python:3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and text file into the container
COPY Assignment_Paragraphs.py paragraphs.txt /app/

# Install NLTK and download the stopwords dataset
RUN pip install nltk
RUN python -m nltk.downloader stopwords

# Run the Python script when the container launches
CMD ["python", "Assignment_Paragraphs.py"]
