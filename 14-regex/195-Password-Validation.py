# 195 : Password Validation
# TODO: Define a function that checks if a given password is valid or not.
# - at least 8 char long
# - contain any sort of letters, numbers, $%#@ (special characters)
# - has to end with a number

import re

# password_pattern = re.compile(r'^[a-zA-Z0-9$%#@]{8,}\d$')
password_pattern = re.compile(r"^[a-zA-Z0-9$%#@]{7,}\d$")


def is_valid_password(password):
    return bool(password_pattern.match(password))


test_passwords = [
    "password",
    "P@ssw0rd",
    "P@ssw0rd!",
    "12345678",
    "12345678!",
    "P@ssw0rd!12345678",
    "P@ssw0rd#12345678",
]

for password in test_passwords:
    print(f"{password}: {is_valid_password(password)}")
