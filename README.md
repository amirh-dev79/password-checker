# 🔐 Password Strength Checker

This is a simple Python script that checks the strength of a password based on common security rules.

## ✅ Features

- Minimum 8 characters
- At least 1 digit
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 special character

## 💻 How to Use

1. Run the script in a terminal:
```bash
python password_checker.py
```

2. Enter your password when prompted.

3. You will see a full breakdown of your password's strength.

## 📂 Example Output

```
--- Password Analysis ---
1. At least 8 characters: OK
2. Contains at least 1 digit: OK
3. Contains at least 1 uppercase letter: NO
4. Contains at least 1 lowercase letter: OK
5. Contains at least 1 special character: OK

❌ Your password is weak. Please create a stronger one.
```

## 📦 How to Improve

- Add password suggestions
- Hide input while typing (with `getpass` module)
- Save strong passwords to a file (with encryption)

## 🔒 Author
@amirh-dev79
