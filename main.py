import hashlib
import random
# import father

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
        for i in range(1, 10):
            rphrase += str(random.randint(1, 100)) # Chooses 10 random integers between 1 and 100 and adds them to rphrase
        password = create_password(rphrase) # Sets password to random password
# Don't touch, might explode       (no guarantees)
    with open("passwords.txt", "a") as f:
        f.write(f"\n{site} | {email} | {password}")

while True:
    c = input(">")
    if c == "cpw":
        password = input("Enter phrase: ")
        print(create_password(password))
    
    elif c == "gpw":
        site = input("Site name: ")
        print(get_password(site))
    
    elif c == "as":
        url = input("Site name: ")
        email = input("Email: ")
        passw = input("Password [--- for auto generate]: ")
        add_site(url, email, passw)
        
        if get_password(url) != None:
            print(f"Added site '{url}' successfully" )
        else:
            print("Error, site not added")

    elif c == "q":
        print("Goodbye")
        input("\n--| PRESS ENTER TO QUIT |--")
        break
