
import re

password = input("Enter password: ")

if len(password) < 12:
    print("Weak: Minimum 12 characters required")

elif not re.search("[a-z]", password):
    print("Weak: Add lowercase letters")

elif not re.search("[A-Z]", password):
    print("Weak: Add uppercase letters")

elif not re.search("[0-9]", password):
    print("Weak: Add numbers")

elif not re.search("[@#$%^&+=]", password):
    print("Weak: Add special characters")

else:
    print("Strong Password")
