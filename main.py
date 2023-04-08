import hashlib
import random
from cryptography.fernet import Fernet
import os
# import father
def write_key():
    key = Fernet.generate_key()
    if  os.path.isfile("key.key"):
        pass
    else:
        with open ("key.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    with open ("key.key", "r") as key_file:
        return key_file.read()

write_key()
key = load_key()


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "r") as file:
        file_data = file.read()
    encoded_data = file_data.encode("utf-8")
    encrypted_data = f.encrypt(encoded_data)
    with open (filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "r") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open (filename, "wb") as file:
        file.write(decrypted_data)

decrypt("passwords.txt", key)

# Creates password using the SHA-256 algorithm
def create_password(phrase):
    phrase = phrase.encode("utf-8")
    pw = hashlib.sha256()
    pw.update(phrase)
    return pw.hexdigest()
# Gets the passwords of an inputted site
def get_password(site):
# Opens passwords.txt and looks through lines for site
# Once it finds it it returns the line
    with open('passwords.txt') as pw_file:
        for line in pw_file:
            if site in line:
                return line
# Adds a site to passwords.txt
def add_site (site, email, password):
# Checks if inputted password is set to autogenerate
    if password[-3:] == '---':
        rphrase = ''
# Chooses 10 random integers between 1 and 100 and adds them to rphrase
        for i in range(1, 10):
            rphrase += str(random.randint(1, 100))
# Sets password to random password using rphrase
        password = create_password(rphrase) 
# Don't touch, might explode       (no guarantees)
    with open("passwords.txt", "a") as f:
        f.write(f"\n{site} | {email} | {password}")



# Prints help menu
print("""
as - Add site, asks for site name, email, and password
cpw - Create Password, asks for password
gpw - Get Password, gets password and email with site name
q - Quit, quits
help - Opens help menu
        """)

while True:
    c = input(">")
# Create Password
    if c == "cpw":
        password = input("Enter phrase: ")
        print(create_password(password))
# Get Password
    elif c == "gpw":
        site = input("Site name: ")
        print(get_password(site))
# Add site
    elif c == "as":
        url = input("Site name: ")
        email = input("Email: ")
        passw = input("Password [--- for auto generate]: ")
        add_site(url, email, passw)
# Validates site was added
        if get_password(url) != None:
            print(f"Added site '{url}' successfully" )
        else:
            print("Error, site not added")
# Help menu
    elif c == "help":
        print("""
as - Add site, asks for site name, email, and password
cpw - Create Password, asks for password
gpw - Get Password, gets password and email with site name
q - Quit, quits
help - Opens help menu
        """)
# Quit
    elif c == "q":
        print("Goodbye")
        input("\n--| PRESS ENTER TO QUIT |--")
        break

encrypt("passwords.txt", key)