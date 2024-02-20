"""Write a program to check the validity of a password. Primary conditions for password validation:
- minimum 8 charecters
- The alphabet must be between [a-z]
- At least one alphabet should be of Upper Case [A-Z]
- At least 1 number or digit between [0-9].
- At least 1 character from [ _ or @ or $ ]."""

password = input("Enter the password: ")

errors = []

if len(password) < 8:
    errors.append("Password must be at least 8 characters long.")
if not any(char.isupper() for char in password):
    errors.append("Password must contain at least one uppercase letter.")
if not any(char.islower() for char in password):
    errors.append("Password must contain at least one lowercase letter.")
if not any(char.isdigit() for char in password):
    errors.append("Password must contain at least one digit.")
if not any(char in ['_', '@', '$'] for char in password):
    errors.append("Password must contain at least one of the characters '_', '@', or '$'.")

if errors:
    print("Invalid Password:")
    for error in errors:
        print(error)
else:
    print("Valid Password")
