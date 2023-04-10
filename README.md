# Password-Manager-WIP
WIP Open Source Password Manager

Works using the python library "hashlib" and encrypts passwords using the SHA-256 algorithm, then stores them in a text file.
Encrypts the text file using "cryptography.fernet" and a randomly generated key.

Ran some passwords through [security.org](www.security.org/):
1. Phrase - github-is-awesome | Time: 85 million quadragintillion years (8.5 * 10^131 years)
2. Phrase - texasbearkat | Time: 85 million quadragintillion years (8.5 * 10^131 years)
3. Phrase - SHA-256 | Time: 85 million quadragintillion years (8.5 * 10^131 years)
As we can see from these results, there is an obvious trend in how much time it takes to crack these passwords, which is **very long.**

# Guide (WINDOWS)
1. Download the zipped release file
2. Unzip it to a folder
3. Make sure key.key does not exist and passwords.txt is not encrypted, if either are true just delete key.key and everything inside passwords.txt
4. Click on top bar where it shows path
5. Type in "cmd"
6. Type "python3 startup.py"
7. Check key.key for a key and that passwords.txt is encrypted
8. Run main.py
9. Validate by typing in "gpw" then "site"; it should return with "site | email | password"

# Guide (LINUX)
1. git clone https://github.com/TexasBearKat/Password-Manager-WIP.git
2. cd Password-Manager-WIP
3. python3 startup.py
4. ls (check for key.key)
5. python3 main.py

# Common Errors
cryptography.fernet.invalidToken Error:
de-encrypt the passwords.txt file if you care about your passwords, I will eventually include one in the install
delete key.key
python3 startup.py
You should have a new key and everything should work again
(I have no clue why this happens so this is more of a bandaid fix)
