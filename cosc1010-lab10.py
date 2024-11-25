# Julian Huerta
# UWYO COSC 1010
# Submission Date: 11/23/24
# Lab 10
# Lab Section: 14
# Sources, people worked with, help given to: 
# The TA
# My brother
# Youtube: https://www.youtube.com/watch?v=NIWwJbo-9_8
# Youtube: https://www.youtube.com/watch?v=i-h0CtKde6w

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.


# You will need to include a try-except-else block in your code.
# - The reading of files needs to occur in the try blocks.

# - Read in the value stored within `hash`.
#   - You must use a try and except block.

# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

target_hash = ""

try:
    hash_file = open('hash', 'r')
    content = hash_file.read()
    target_hash = content.strip()
    target_hash = target_hash.lower()
    hash_file.close()

except Exception as e:
    print("Attempting to read the password file...")


passwords = []

try:
    password_file = open('rockyou.txt', 'r')
    lines = password_file.readlines()
    for line in lines:
        cleaned_password = line.strip()
        passwords.append(cleaned_password)
    password_file.close()
except Exception as e:
    found = False
for password in passwords:
    hashed_password = ""
    try:
        encoded_password = password.encode()
        hashed_password = sha256(encoded_password).hexdigest()
        hashed_password = hashed_password.lower()
        print(f"Hashed password: {hashed_password}")

    except Exception as e:
        print(f"Error hashing the password: {e}")
        continue
    if hashed_password == target_hash:
        print(f"Correct password is: {password}")
        found = True
        break

