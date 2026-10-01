# Password Auditor – IT610 Midterm Project  

- **Author:** Harsh Patel
- IT 610:851 – NJIT
- **Project:** Docker-Based Password Auditor

---

# Overview

This project provides a command‑line password auditing utility designed specifically for system administrators and end users using Docker. 
The user enters a username and a password **(which is hidden)**, and the tool:

- Evaluates the password against strict complexity rules
- Generates a HTML report to review the audit
  
The entire application runs inside a **Docker container**.

---

# Project Structure

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

The report is generated at: **`/output/Password_Audit_Report.html`** under the /scanner folder.


Every time the docker is ran the results are added and updated to the HTML report as a table containing:

- Username
- Hashed Password
- Weak Password? (YES/NO)
- Failed Requirements
  
The HTML report is automatically generated after the docker image is built and ran successfully.

---
# Author  
**Harsh Patel**  
IT610:851 – NJIT

---
