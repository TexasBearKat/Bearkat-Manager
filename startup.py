from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    if  os.path.isfile("key.key"):
        pass
    else:
        with open ("key.key", "wb") as key_file:
            key_file.write(key)

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "r") as file:
        file_data = file.read()
    encoded_data = file_data.encode("utf-8")
    encrypted_data = f.encrypt(encoded_data)
    with open (filename, "wb") as file:
        file.write(encrypted_data)

def load_key():
    with open ("key.key", "r") as key_file:
        return key_file.read()

write_key()
key = load_key()
encrypt("passwords.txt", key)