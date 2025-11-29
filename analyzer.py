import string

# Test passwords
password_list = ["123456", "Emin2025!", "hello", "SuperStrongPass@2025", "password", "Qwerty12"]

# Common passwords
COMMON_PASSWORDS = ["123456", "password", "qwerty", "admin", "111111", "abc123", "letmein"]

results = []

for pwd in password_list:
    score = 0
    issues = []

    if len(pwd) >= 12:
        score += 1
    else:
        issues.append("Length is less than 12 characters")

    if any(c.isupper() for c in pwd):
        score += 1
    else:
        issues.append("No uppercase letters")

    if any(c.islower() for c in pwd):
        score += 1
    else:
        issues.append("No lowercase letters")

    if any(c.isdigit() for c in pwd):
        score += 1
    else:
        issues.append("No numbers")

    symbols = string.punctuation
    if any(c in symbols for c in pwd):
        score += 1
    else:
        issues.append("No special characters")

    if pwd.lower() in COMMON_PASSWORDS:
        issues.append("This password is in the common passwords list")

    # Determine color: red=weak, yellow=medium, green=strong
    if score <= 2:
        color = "red"
    elif score == 3 or score == 4:
        color = "orange"
    else:
        color = "green"

    results.append({"password": pwd, "score": score, "issues": issues, "color": color})

# Generate HTML report
with open("report.html", "w", encoding="utf-8") as f:
    f.write("<html><body style='font-family: Arial, sans-serif;'>")
    f.write("<h1>Password Strength Report</h1>")

    for res in results:
        f.write(f"<h3 style='color:{res['color']}'>{res['password']}</h3>")
        f.write(f"<p>Score: {res['score']}/5</p>")

        if res["issues"]:
            f.write("<ul>")
            for issue in res["issues"]:
                f.write(f"<li>{issue}</li>")
            f.write("</ul>")
        else:
            f.write("<p>No issues — strong password.</p>")

    f.write("</body></html>")

print("Analysis complete! Open report.html to see results.")
