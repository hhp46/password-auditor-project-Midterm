#Tells Docker which base image to start from 
FROM python:3.11-slim

#Set working directory
WORKDIR /scanner

# Copy Python script locally from the project folder 
COPY password_auditor.py /scanner/password_auditor.py

#Installs Python package which is needed for the script (PASSWORD HASHING)
RUN pip install argon2-cffi

#Default program set that runs when the container starts
ENTRYPOINT ["python", "/scanner/password_auditor.py"]

