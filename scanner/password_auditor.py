# -*- coding: utf-8 -*-
import os
import re
from datetime import datetime
from zoneinfo import ZoneInfo
from getpass import getpass
from argon2 import PasswordHasher

# Report output location
REPORT_PATH = "/output/Password_Audit_Report.html"

# Argon2 hasher
ph = PasswordHasher()


# -----------------------------
#  Password rule checks
# -----------------------------
def check_password_rules(username, password):
    """
    Evaluate password complexity based on a few basic rules.
    Returns (is_strong, list_of_failed_requirements) 
    """
    failures = []
    pw_lower = password.lower()
    user_lower = username.lower()

    # length check
    if not (8 <= len(password) <= 14):
        failures.append("Password must be between 8 and 14 characters long")

    # uppercase letter
    
    if not any(c.isupper() for c in password):
        failures.append("Password must contain at least one uppercase letter")
   
    # lowercase
    if not any(c.islower() for c in password):
        failures.append("Password must contain at least one lowercase letter")
   
    # digit
    if not any(c.isdigit() for c in password):
        failures.append("Password must contain at least one numeric digit")
    
    # special character
    if not re.search(r"[^A-Za-z0-9]", password):
        failures.append("Password must contain at least one special character")

    # username in password
    if user_lower in pw_lower:
        failures.append("Password cannot contain the username")

    # repeated characters
    if re.search(r"(.)\1\1", password):
        failures.append("Password cannot contain a character repeated more than twice in a row")

    return len(failures) == 0, failures
    

# ---------------------------------------------------------
# HTML for the table row
# ---------------------------------------------------------
def create_row(username, hashed_pw, failures):
    weak_flag = "YES" if failures else "NO"
    color = "#e74c3c" if failures else "#2ecc71"  # red or green badge
    failure_text = "<br>".join(failures) if failures else "None"

    return f"""
    <tr>
        <td>{username}</td>
        <td style="word-break: break-all;">{hashed_pw}</td>
        <td style="text-align:center;">
            <span style="
                background:{color};
                color:white;
                padding:6px 12px;
                border-radius:6px;
                font-weight:bold;">
                {weak_flag}
            </span>
        </td>
        <td>{failure_text}</td>
    </tr>
    """


# -----------------------------
# HTML Report Styling
# -----------------------------
def HTML_REPORT(username, hashed_pw, failures):
    timestamp = datetime.now(ZoneInfo("America/New_York")).strftime("%m-%d-%Y %H:%M")
    row_html = create_row(username, hashed_pw, failures)

    # If report does NOT exist, create new HTML file
    if not os.path.exists(REPORT_PATH):
        with open(REPORT_PATH, "w") as f:
            # Basic HTML template — keeping it simple and readable
            f.write(f"""
<!DOCTYPE html>
<html>
<head>
<title>Password Audit Report</title>

<style>
    body {{
        font-family: Arial, Helvetica, sans-serif;
        background: #f4f7fa;
        margin: 0;
        padding: 20px;
    }}

    h1 {{
        text-align: center;
        margin-bottom: 0px;
        color: #2c3e50;
    }}

    p.timestamp {{
        text-align: center;
        font-size: 14px;
        color: #34495e;
        margin-top: 5px;
        margin-bottom: 25px;
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
        background: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
    }}

    th {{
        background: #3498db;
        color: white;
        padding: 12px;
        text-align: center;
        border-right: 3px solid #1f6fa5;
    }}

    td {{
        padding: 12px;
        border-bottom: 1px solid #e0e0e0;
        border-right: 3px solid #d1d1d1;
        vertical-align: top;
    }}

    td:last-child,
    th:last-child {{
    border-right: none;
    }}

    tr:nth-child(even) {{
    background: #f2f6fc;
    }}

    tr:hover {{
    background: #e8f1ff;
    }}
    
</style>

</head>
<body>

<h1>Password Audit Report</h1>
<p class="timestamp">Report Generated: {timestamp} (EST)</p>

<table>
<tr>
    <th>Username</th>
    <th>Hashed Password</th>
    <th>Weak Password?</th>
    <th>Requirements Failing</th>
</tr>
{row_html}
</table>

</body>
</html>
            """)

# -----------------------------
# Message on screen after audit is complete
# -----------------------------
        print(f"\nNew report created at: {REPORT_PATH} which is under the scanner folder.")
        return

    # If report exists, update timestamp and append new row
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    # Update timestamp (quick regex replace)
    updated_ts = f"<p class=\"timestamp\">Report Updated: {timestamp} (EST)</p>"
    content = re.sub(r"<p class=\"timestamp\">.*?</p>", updated_ts, content)

    # Append row before </table>
    content = content.replace("</table>", row_html + "</table>")

    # Write updated file
    with open(REPORT_PATH, "w") as f:
        f.write(content)

    print(f"\nReport updated at: {REPORT_PATH} which is under the scanner folder.")


# -----------------------------------------
#  Main Program - Interactive via cmdline
# -----------------------------------------
def main():
    print("Auditing for a Secure Password")
    username = input("Enter your username: ").strip()
    password = getpass("Enter your password (HIDDEN): ").strip()

    # Input cant be empty
    if not username:
        print("Username cannot be empty. Run 'python password_auditor.py' again.")
        return
    
    if not password:
        print("Password cannot be empty. Run 'python password_auditor.py' again.")
        return
        
    strong, failures = check_password_rules(username, password)
    hashed_pw = ph.hash(password)

    HTML_REPORT(username, hashed_pw, failures)
    
# -----------------------------
# Message on screen after audit is complete and report is generated
# -----------------------------
    if strong:
        print("\nPassword is STRONG and meets the complexity requirements. Details logged in the report.")
    else:
        print("\nPassword is WEAK and must meet the complexity requirements. Details logged in the report.")


if __name__ == "__main__":
    main()
