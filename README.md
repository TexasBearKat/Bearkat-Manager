# Password-Manager-WIP
WIP Open Source Password Manager

Works using the python library "hashlib" and encrypts passwords using the SHA-256 algorithm, then stores them in a text file.
There's not much to it.

# Guide
1. Download the zipped release file
2. Unzip it to a folder
3. Make sure key.key does not exist and passwords.txt is not encrypted
3.1 If key.key exists delete it
3.2 If passwords.txt is encrypted then delete everything in the file
4. Run startup.py
5. Check key.key for a key and that passwords.txt is encrypted
6. Run main.py
7. Validate by typing in "gpw" then "site"; it should return with "site | email | password"
