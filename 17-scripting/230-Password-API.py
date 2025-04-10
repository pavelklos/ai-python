# 230 : Password API

# [checkmypass.py] -------------------------------------------------------------

# > pip3 install requests
# > python3 checkmypass.py password

import hashlib  # TODO: to hash password  # hashlib.sha1()
import sys  # TODO: to get command line arguments  # sys.argv

import requests  # TODO: to make HTTP requests  # requests.get()

# TODO: check API response: '400 Bad Request' ----------------------------------
# TODO: - we need to use hash of the password, not the password itself
# url = 'https://api.pwnedpasswords.com/range/' + 'password123'
# res = requests.get(url)
# print(res)  # TODO: <Response [400]> = '400 Bad Request'

# TODO: [SHA1 Hash Generator] --------------------------------------------------
# - https://passwordsgenerator.net/sha1-hash-generator/
# - password123: [SH1] CBFDAC6008F9CAB4083784CBD1874F76618D2A97

# TODO: [K-anonymity] ----------------------------------------------------------
# - https://en.wikipedia.org/wiki/K-anonymity
# - is technique to protect privacy of individuals in large datasets
# - get only first 5 characters of the hash and send it to the API

# TODO: check API response: '200 OK' -------------------------------------------
# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'
# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# res = requests.get(url)
# print(res)  # TODO: <Response [200]> = '200 OK'


# TODO: get API response data by request ---------------------------------------
def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:  # TODO: 200 means all good!
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the api and try again"
        )
    return res


# TODO: get password leaks count from API response -----------------------------
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


# TODO: check password if exists in API response -------------------------------
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    # print(f'password (SHA1): {sha1password}')
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


# TODO: main function ----------------------------------------------------------
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times... you should probably change your password!"
            )
        else:
            print(f"{password} was NOT found. Carry on!")
    return "done!"


# if __name__ == '__main__':
#   sys.exit(main(sys.argv[1:]))
#   # sys.exit() make sure the program ends to the command line at last.

# TODO: run main function ------------------------------------------------------
main(["password123", "password", "123", "dotnet", "heslo", "doTneT"])
# password123 was found 294737 times... you should probably change your password!
# password was found 10434004 times... you should probably change your password!
# 123 was found 1783558 times... you should probably change your password!
# dotnet was found 7873 times... you should probably change your password!
# doTneT was NOT found. Carry on!

"""
this website takes the first 5 digit of the 'SHA 1 hash'
so we actually generate a SHA 1 hash of our password and then just pass the first five digits of the hash
so we are keeping safe our hash, so that no one can even backtrace the password using our hash.
and this website list all the hash starting with the 5 digits we have passed, and we can then manually check whether our 
password has been hacked or not
"""

# TODO: check functions
# response = request_api_data('CBFDA')         # TODO: <Response [200]> for 5 chars from hashed password
# print(response.url)
# print(response.status_code)
# # print(response.text)                              # TODO: list of hashes starting with 'CBFDA'
# # CBFDAC6008F9CAB4083784CBD1874F76618D2A97          # our hashed password
# # CBFDA                                             # request (first 5 chars of the hashed password)
# # C6008F9CAB4083784CBD1874F76618D2A97:294737        # response (last 35 chars of the hashed password):count
# result = pwned_api_check('password123')
# print(result)                                       # TODO: 294737
