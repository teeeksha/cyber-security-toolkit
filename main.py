from tools.encryption_tool import encrypt
from tools.hash_generator import generate_hash
from tools.password_checker import check_password

def menu():
    print("\n--- Cyber Security Toolkit ---")
    print("1. Encrypt Text")
    print("2. Generate Hash")
    print("3. Check Password Strength")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '1':
        text = input("Enter text: ")
        print("Encrypted:", encrypt(text))

    elif choice == '2':
        text = input("Enter text: ")
        print("Hash:", generate_hash(text))

    elif choice == '3':
        pwd = input("Enter password: ")
        print(check_password(pwd))

    elif choice == '4':
        break

    else:
        print("Invalid choice")