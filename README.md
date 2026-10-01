# Password Auditor – IT610 Midterm Project  

- **Author:** Harsh Patel
- **Course:** IT 610:851 – NJIT
- **Project:** Docker-Based Password Auditor (Single Container)

---

## Overview

This project provides a command‑line password auditing utility designed specifically for system administrators and end users using Docker. 
The user enters a username and a password **(which is hidden)**, and the tool:

- Evaluates the password against strict complexity rules
- Generates a HTML report to review the audit
  
The entire application runs inside a **Docker container**.

---

## Project Structure

```
password-auditor-project/
│
└── scanner/
      ├── Dockerfile
      ├── password_auditor.py
      └── output/                            (generated automatically)
            └── Password_Audit_Report.html   (generated automatically)
```
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
## Author  
**Harsh Patel**  
IT610:851 – NJIT

---
