import hashlib
import random

def create_password(phrase):
    phrase = phrase.encode("utf-8")
    pw = hashlib.sha256()
    pw.update(phrase)
    return pw.hexdigest()

def get_password(site):
    with open('passwords.txt') as pw_file:
        for line in pw_file:
            if site in line:
                return line
        
def add_site (site, email, password):
    if password[-3:] == '---':
        rphrase = ''
        for i in range(1, 10):
            rphrase += str(random.randint(1, 100))
        password = create_password(rphrase)
        
    f = open("passwords.txt", "a")
    f.write(site+" | "+email+" | "+password)

while True:
    c = input(">")
    if c == "cpw":
        password = input("Enter phrase: ")
        print(create_password(password))
    elif c == "gpw":
        url = input("Site name: ")
        print(get_password(url))
        url = 0
    elif c == "as":
        url = input("Site name: ")
        email = input("Email: ")
        passw = input("Password [--- for auto generate]: ")
    elif c == "q":
        print("Goodbye")
        input("\n--| PRESS ANY KEY TO QUIT |--")
        break