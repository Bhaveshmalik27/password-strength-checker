import re

def check_password_strength(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password)
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if all([length, digit, upper, lower, special]):
        return "Strong"
    elif length and (upper or lower) and digit:
        return "Medium"
    else:
        return "Weak"

# User input
user_password = input("Enter your password: ")
result = check_password_strength(user_password)
print("Password Strength:", result)
