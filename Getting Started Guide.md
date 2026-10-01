***
# **GETTING STARTED GUIDE – PASSWORD AUDITOR MIDTERM PROJECT**

- **Author:** Harsh Patel
- **Course:** IT610:851 – NJIT
- **Project:** Docker-Based Password Auditor
***

## **Overview**
The Midterm Project **Password Auditor** evaluates password strength using complexity rules based on the NJ State SISM Policy which I have implemented. 

It generates an HTML report and runs entirely inside Docker so no additional Python installation required.

---

## **Requirements**
- Docker Desktop (Windows/macOS/Linux)  
- Terminal / PowerShell access  
- Permission to mount volumes
- Correct working directory

---

## **Project Structure**
```
password-auditor-project/
│
└── scanner/
      ├── Dockerfile
      ├── password_auditor.py
      └── output/                            (generated automatically)
            └── Password_Audit_Report.html   (generated automatically)
```

❗ The /output directory and the HTML report will be generated automatically once the Docker image is built and run successfully inside the container.

---

## **Before You Begin ❗**
Make sure **Docker Desktop is running** before you start.  
If Docker Desktop is not running, the build and run commands will FAIL.
* Run all commands from inside the /scanner folder in the project folder: **`C:\Users\<USERNAME>\Desktop\password-auditor-project-Midterm\scanner`**
---

## **Password Rules**
A password is considered **valid** only if it meets all of the following complexity requirements:

- 8–14 characters  
- At least one uppercase  
- At least one lowercase  
- At least one digit  
- At least one special character  
- Does **not** contain the username
- No character repeated 3+ times consecutively  

---
# STEPS
---

## **1. Build the Docker Image**

Navigate into the folder containing the Dockerfile (inside `/scanner`):

```
cd path/to/password-auditor-project/scanner
```

Build the image:

```
docker build -t password-auditor .
```
Build the image using --no-cache: (Recommended to use -  Dont forget the . at the end of the command) ❗
```
docker build --no-cache -t password-auditor .
```

---

## **2. Run the Auditor Inside the Container** ❗
2.1 - Start a shell inside the container and mount the output directory:

```
docker run -it --entrypoint bash -v ${PWD}/output:/output password-auditor
```

2.2 - Run the auditor manually:

```
python password_auditor.py
```

Enter your username and password when prompted.  
Your password input is **HIDDEN** for security.  
The report will be saved to `/output`.

---

## **3. Exit the Container** ❗
Inside the container enter:

```
exit
```

or press **Ctrl + D**.

---

## **4. View Your HTML Report**
Open:

```
output/Password_Audit_Report.html
```

The report includes:

- Username  
- Argon2 hashed password  
- Weak/Strong status  
- Failed rules  
- Timestamp  (Updated on every run)

The report updates on each run. Data for each run is put into a table.

---

## **5. Troubleshooting Tips**

#### **(5.1) Report not generating**
Check the volume mount:

```
-v ${PWD}/output:/output
```
#### **(5.2) Other commands to try if you get volume errors in PowerShell or CMD. Windows has different shells with different rules**

```
docker run -it --entrypoint bash -v "${PWD}/output:/output" password-auditor
docker run -it --entrypoint bash -v "$($PWD.Path)/output:/output" password-auditor
docker run -it --entrypoint bash -v "%cd%/output:/output" password-auditor
```

#### **(5.3) Build running too fast (cached layers)**
Force rebuild:

```
docker build --no-cache -t password-auditor .
```

#### **(5.4) Wrong working directory**

All commands must be executed from where the Dockerfile lives.  
For this project repo, it's under `/scanner`.

```
path/to/password-auditor-project/scanner
```

---

## **Best Practices**
- Use during onboarding or periodic password audits  
- Store reports securely  
- Address weak passwords promptly  
- Archive reports regularly  
- Never share hashed passwords publicly  
