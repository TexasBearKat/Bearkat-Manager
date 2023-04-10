# Password-Manager-WIP
WIP Open Source Password Manager

Works using the python library "hashlib" and encrypts passwords using the SHA-256 algorithm, then stores them in a text file.
Encrypts the text file using "cryptography.fernet" and a randomly generated key.

Ran some passwords through [security.org](www.security.org/):
1. Phrase - github-is-awesome | Time: 85 million quadragintillion years (8.5 * 10^131 years)
2. Phrase - texasbearkat | Time: 85 million quadragintillion years (8.5 * 10^131 years)
3. Phrase - SHA-256 | Time: 85 million quadragintillion years (8.5 * 10^131 years)
As we can see from these results, there is an obvious trend in how much time it takes to crack these passwords, which is **very long.**

# Guide
1. Download the zipped release file
2. Unzip it to a folder
3. Make sure key.key does not exist and passwords.txt is not encrypted
3.1 If key.key exists delete it
3.2 If passwords.txt is encrypted then delete everything in the file
4. Click on top bar where it shows path
5. Type in "cmd"
6. Type "python3 startup.py"
7. Check key.key for a key and that passwords.txt is encrypted
8. Run main.py
9. Validate by typing in "gpw" then "site"; it should return with "site | email | password"

Thank you for using my code
