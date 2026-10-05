# -*- coding: utf-8 -*-
import os
import re
from argon2 import PasswordHasher
from getpass import getpass
from datetime import datetime
from zoneinfo import ZoneInfo

REPORT_PATH = "/output/Password_Audit_Report.html"
ph = PasswordHasher()


# -----------------------------
#  Password Evaluation RULES
# -----------------------------
def evaluate_password(username, passwd):
    requirement = []
    passwd_lower = passwd.lower()
    user_lower = username.lower()

    if len(passwd) < 8 or len(passwd) > 14:
        requirement.append("Password must be between 8 and 14 characters long")
    if not any(c.isupper() for c in passwd):
        requirement.append("Password must contain at least 1 uppercase letter")
    if not any(c.islower() for c in passwd):
        requirement.append("Password must contain at least 1 lowercase letter")
    if not any(c.isdigit() for c in passwd):
        requirement.append("Password must contain at least 1 numeric digit")
    if not re.search(r"[^A-Za-z0-9]", passwd):
        requirement.append("Password must contain at least 1 special character")
    if user_lower in passwd_lower:
        requirement.append("Password cannot contain the username")
    if re.search(r"(.)\1\1", passwd):
        requirement.append("Password cannot contain a character repeated more than twice in a row")

    strong = len(requirement) == 0
    return strong, requirement


# -----------------------------
# Password Column Styling 
# -----------------------------
def create_table_row(username, hashed_password, requirement):
    weak = "YES" if requirement else "NO"
    badge_color = "#e74c3c" if requirement else "#2ecc71"  # red / green

    requirement_text = "<br>".join(requirement) if requirement else "None"

    return f"""
    <tr>
        <td>{username}</td>
        <td style="word-break: break-all;">{hashed_password}</td>
        <td style="text-align:center;">
            <span style="
                background:{badge_color};
                color:white;
                padding:6px 12px;
                border-radius:6px;
                font-weight:bold;">
                {weak}
            </span>
        </td>
        <td>{requirement_text}</td>
    </tr>
    """


# -----------------------------
# HTML Report Styling
# -----------------------------
def HTML_REPORT(username, hashed_password, requirement):
    timestamp = datetime.now(ZoneInfo("America/New_York")).strftime(
        "%m-%d-%Y %H:%M"
    )

    row_html = create_table_row(username, hashed_password, requirement)

    # If report does NOT exist, create new HTML file
    if not os.path.exists(REPORT_PATH):
        with open(REPORT_PATH, "w") as f:
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
        font-size: 32px;
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
        font-size: 16px;
        border-right: 3px solid #1f6fa5;
    }}

    td {{
        padding: 12px;
        border-bottom: 1px solid #e0e0e0;
        border-right: 3px solid #d1d1d1;
        vertical-align: top;
        font-size: 15px;
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

        print(f"\nNew report created: {REPORT_PATH}")
        return

    # If report exists, update timestamp and append new row
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    # Update timestamp
    new_timestamp = f"<p class=\"timestamp\">Report Updated: {timestamp} (EST)</p>"
    content = re.sub(
        r"<p class=\"timestamp\">.*?</p>",
        new_timestamp,
        content
    )

    # Append row before </table>
    content = content.replace("</table>", row_html + "</table>")

    # Write updated file
    with open(REPORT_PATH, "w") as f:
        f.write(content)

    print(f"\nReport updated at: {REPORT_PATH}")


# -----------------------------------------
#  Main Program - Interactive via cmdline
# -----------------------------------------
def main():
    print("Auditing for a Secure Password")
    username = input("Enter your username: ").strip()
    password = getpass("Enter your password (HIDDEN): ").strip()

    strong, requirement = evaluate_password(username, password)
    hashed = ph.hash(password)

    HTML_REPORT(username, hashed, requirement)

    if not strong:
        print("\nPassword is WEAK and must meet the complexity requirements. It is logged in the report.")
    else:
        print("\nPassword is STRONG and meets the complexity requirements. It is logged in the report.")


if __name__ == "__main__":
    main()
