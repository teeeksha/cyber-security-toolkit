from cryptography.fernet import Fernet

# Key generate
key = Fernet.generate_key()
cipher = Fernet(key)

print("Secret Key (save this):", key.decode())

text = input("Enter text: ").encode()

# Encrypt
encrypted = cipher.encrypt(text)
print("\nEncrypted Data:", encrypted.decode())

# Decrypt
decrypted = cipher.decrypt(encrypted)
print("Decrypted Data:", decrypted.decode())
