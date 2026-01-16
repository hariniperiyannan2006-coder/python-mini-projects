# Password Strength Checker
password = input("Enter your password: ")
strength = 0
if len(password) >= 8:
    strength += 1
if any(char.isdigit() for char in password):
    strength += 1
if any(char.isupper() for char in password):
    strength += 1
if any(char in "!@#$%^&*()" for char in password):
    strength += 1
# Final result
if strength == 4:
    print("Password Strength: Strong")
elif strength == 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")
