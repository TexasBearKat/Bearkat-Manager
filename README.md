# | Bearkat Manager |
WIP Open Source Password Manager

Works using the python library "hashlib" and encrypts passwords using the SHA-256 algorithm, then stores them in a text file.
Encrypts the text file using "cryptography.fernet" and a randomly generated key.

Ran some passwords through [security.org](www.security.org/):
1. Phrase - github-is-awesome | Time: 85 million quadragintillion years (8.5 * 10<sup>131</sup> years)
2. Phrase - texasbearkat | Time: 85 million quadragintillion years (8.5 * 10<sup>131</sup> years)
3. Phrase - SHA-256 | Time: 85 million quadragintillion years (8.5 * 10<sup>131</sup> years)
As we can see from these results, there is an obvious trend in how much time it takes to crack these passwords, which is **very long.**

### Todo
- [x] Create more secure passwords
- [ ] Encrypt and decrypt only when necessary
- [ ] Create macOS guide
- [ ] Create repl.it guide

## Guide (WINDOWS)
1. Download the zipped release file
2. Install python cryptography package `pip install cryptography`
3. Excract zip file
4. On the top bar (where the path is), click it and type cmd, press enter
5. Type in 
```
python3 startup.py
python3 main.py
```  
6. Check for key.key, if it isn't there rerun `python3 startup.py`
7. You should now have it up and running

## Guide (LINUX)
1. Access command line
2. cd into whatever directory you want the folder in
3. Run this:
```
$ pip install cryptography
$ git clone https://github.com/TexasBearKat/Bearkat-Manager.git
$ cd Bearkat-Manager
$ python3 startup.py
$ python3 main.py
```
It should be started up and working.

## Guide (REPL.IT)
1. Make a new python repl
2. Go to the shell tab (Do this by clicking the + button and searching "Shell")
3. Follow linux guide

## Common Errors
cryptography.fernet.invalidToken Error:
This happens when the main.py program shuts down unexpectedly, and causes the passwords.txt file to go unencrypted.
To fix this, just rerun startup.py:
`python3 startup.py`

Credits:
TexasBearKat - Sole contributor and owner
GooseiverseIndex - Moral support and funny comment man
