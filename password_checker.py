
from getpass import getpass

password = getpass("Enter a test password: ")

checks = {
    "At least 12 characters": len(password) >= 12,
    "Uppercase letter": any(c.isupper() for c in password),
    "Lowercase letter": any(c.islower() for c in password),
    "Number": any(c.isdigit() for c in password),
    "Special character": any(c in "!@#$%^&*()-_+" for c in password)
}

print("\n=== PASSWORD SECURITY CHECKER ===")

score = 0

for check, passed in checks.items():
    if passed:
        print("[PASS]", check)
        score += 1
    else:
        print("[FAIL]", check)

print("\nChecks passed:", score, "out of", len(checks))

if score <= 2:
    print("Result: Needs improvement")
elif score <= 4:
    print("Result: Fair")
else:
    print("Result: All basic checks passed")
