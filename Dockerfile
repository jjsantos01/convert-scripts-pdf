# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
RUN apt-get update
RUN apt-get -y install wkhtmltopdf

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy files
COPY convert_scripts_to_pdf.py .
COPY convert_scripts_to_pdf_highlight.py .
