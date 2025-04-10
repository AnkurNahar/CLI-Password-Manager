from cryptography.fernet import Fernet

# Generating a secret key
key = Fernet.generate_key()

# Printing secret key to save securely
print("Encryption key:", key.decode())

