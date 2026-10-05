# Password Auditor – IT610 Midterm Project  

- **Author:** Harsh Patel
- **Course:** IT 610:851 – NJIT
- **Project:** Docker-Based Password Auditor (Single Container)

---

## Overview

This Midterm Project (using Docker) provides a command‑line password auditing utility designed specifically for system administrators and end users. 
The user enters a username and a password **(which is hidden)**, which they want to see if its valid/complex, and the tool:

1. Evaluates the password against strict complexity rules
2. Generates a HTML report to review the audit
  
- The entire application runs inside a **Docker container**.

---

## Project Structure

```
password-auditor-project-Midterm/
│
└── scanner/
      ├── Dockerfile
      ├── password_auditor.py
      └── output/                            (generated automatically)
            └── Password_Audit_Report.html   (generated automatically)


```
❗The /output directory and the HTML report will be generated automatically once the Docker image is built and run successfully inside the container.

---



## HTML Report

The report is generated at: **`../scanner/output/Password_Audit_Report.html.`**

Each time the scanner container is run, a new entry is added to the HTML table containing:

- Username
- Hashed Password (Argon2)
- Weak Password? (YES/NO)
- Failed Requirements
- Timestamp
  
The HTML report is automatically generated after the docker image is built and ran successfully.

---

## **❗ Note:** 
Use the `Getting Started Guide.md` file to walkthrough the project. 

---

## Author  
**Harsh Patel**  
IT610:851 – NJIT

---
