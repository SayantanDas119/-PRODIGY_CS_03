def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        strength = "Weak"
    elif len(password) < 12:
        strength = "Medium"
    else:
        strength = "Strong"

    # Check character types
    uppercase_count = sum(1 for c in password if c.isupper())
    lowercase_count = sum(1 for c in password if c.islower())
    number_count = sum(1 for c in password if c.isdigit())
    symbol_count = sum(1 for c in password if not c.isalnum())

    # Adjust strength based on character types
    if uppercase_count + lowercase_count + number_count + symbol_count < 3:
        strength = min(strength, "Weak")

    return strength

# Get password input
password = input("Enter your password: ")

# Check password strength
strength = check_password_strength(password)
print("Password strength:", strength)
