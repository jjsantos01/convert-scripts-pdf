# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
COPY requirements.txt .
COPY convert_scripts_to_pdf.py .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run convert_scripts_to_pdf.py when the container launches
ENTRYPOINT ["python", "./convert_scripts_to_pdf.py"]
