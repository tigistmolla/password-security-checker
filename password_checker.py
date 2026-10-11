
"""
Password Security Checker
Educational Python project by Tigist Haileeyesus Molla.
"""

password = "Hello@123456"  # Sample password for testing only

checks = {
    "At least 12 characters": len(password) >= 12,
    "Uppercase letter": any(c.isupper() for c in password),
    "Lowercase letter": any(c.islower() for c in password),
    "Number": any(c.isdigit() for c in password),
    "Special character": any(c in "!@#$%^&*()-_+" for c in password),
}

print("=== PASSWORD SECURITY CHECKER ===")
print("Password: " + "*" * len(password))
print()

score = 0

for check, passed in checks.items():
    if passed:
        print("[PASS]", check)
        score += 1
    else:
        print("[FAIL]", check)

print()
print("Checks passed:", score, "out of", len(checks))

if score <= 2:
    print("Result: Needs improvement")
elif score <= 4:
    print("Result: Fair")
else:
    print("Result: All basic checks passed")

print()
print("Note: This is an educational checker,")
print("not a guarantee of password security.")
