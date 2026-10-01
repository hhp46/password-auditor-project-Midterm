#Tells Docker which base image to start from 
FROM python:3.11-slim

#Set working directory
WORKDIR /scanner

# Copy Python script from the project folder to local 
COPY password_auditor.py /scanner/password_auditor.py

#Installs Python package needed for the script (HASHING)
RUN pip install argon2-cffi

#Set default program that runs when the container starts
ENTRYPOINT ["python", "/scanner/password_auditor.py"]

