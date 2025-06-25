# Password Strength Checker

# List of special characters
special_chars = "!@#$%^&*()_-+={}[];:,.<>?/|\\"

# Ask user to enter a password
password = input("Enter your password: ")

# Check each condition
is_long_enough = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_special = any(char in special_chars for char in password)

# Show detailed results
print("\n--- Password Analysis ---")
print("1. At least 8 characters:", "OK" if is_long_enough else "NO")
print("2. Contains at least 1 digit:", "OK" if has_digit else "NO")
print("3. Contains at least 1 uppercase letter:", "OK" if has_upper else "NO")
print("4. Contains at least 1 lowercase letter:", "OK" if has_lower else "NO")
print("5. Contains at least 1 special character:", "OK" if has_special else "NO")

# Final verdict
if all([is_long_enough, has_digit, has_upper, has_lower, has_special]):
    print("\n✅ Your password is secure.")
else:
    print("\n❌ Your password is weak. Please create a stronger one.")
