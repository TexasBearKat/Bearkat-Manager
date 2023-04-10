import hashlib
import random
from cryptography.fernet import Fernet
import os
# import father

# -------- ENCRYPTION ---------

# Writes key after checking whether or not there is a key
def write_key():
    key = Fernet.generate_key()
# Checks if key.key is a file
    if os.path.isfile("key.key"):
        pass
    else:
        with open ("key.key", "wb") as key_file:
            key_file.write(key)

# Reads key.key file for key
def load_key():
    with open ("key.key", "r") as key_file:
        return key_file.read()


write_key()
key = load_key()


# Encrypts the file using Fernet and the key
def encrypt(filename, key):
    f = Fernet(key)
# Creates a fernet object using the key
    with open(filename, "r") as file:
        file_data = file.read()
# Encodes the data into bytes then encrypts it
    encoded_data = file_data.encode("utf-8")
    encrypted_data = f.encrypt(encoded_data)
# Write back into file
    with open (filename, "wb") as file:
        file.write(encrypted_data)


# Decrypts file using Fernet and the key
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "r") as file:
        encrypted_data = file.read()
# Same process as encryption but decrypts instead of encrypts
    encoded_data = encrypted_data.encode("utf-8")
    decrypted_data = f.decrypt(encoded_data)
    with open (filename, "wb") as file:
        file.write(decrypted_data)

# Decrypt passwords.txt with your generated key
decrypt("passwords.txt", key)

# ------ MAIN FUNCTIONS --------------

def capitalize_every_other(string):
    result = ""
    prev_char_cap = False
# For character in string, if the last one was uppercase then make this one lowercase. ELse, make it uppercase
    for char in string:
        if prev_char_cap:
            result = result + char.lower()
        else:
            result = result + char.upper()
        prev_char_cap = not prev_char_cap
    return result

def add_symbols(string):
    result = ""
    nums = ['3','6','9',]
# Looks through characters and if they are in nums then apply changes to result.
    for char in string:
        if char in nums:
            if char == "3":
                result = result + "--"
            if char == "6":
                result = result + "--_"
            if char == "9":
                result = result + "-__-"
        result = result + char
    return result

# Creates password using the SHA-256 algorithm
def create_password(phrase):
    phrase = phrase.encode("utf-8")
    pw = hashlib.sha256()
    pw.update(phrase)
    hexpw = pw.hexdigest()
    cappw = capitalize_every_other(hexpw)
    sympw = add_symbols(cappw)
    if len(sympw) > 79:
        sympw = sympw[0:79]
    return sympw

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
*** MAKE SURE NOT TO ADD ARGS ***
        """)

# ------- COMMANDS ----------

while True:
    c = input("PM>> ")
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
            print(f"Added site '{url}' successfully")
            print(f"Password is {get_password(url)}")
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


# Encrypt the file when the program is closed
encrypt("passwords.txt", key)
