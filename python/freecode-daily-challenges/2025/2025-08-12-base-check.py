# Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

# The string may contain integers, and uppercase or lowercase characters.
# The check should be case-insensitive.
# The base can be any number 2-36.
# A number is valid if every character is a valid digit in the given base.
# Example of valid digits for bases:
# Base 2: 0-1
# Base 8: 0-7
# Base 10: 0-9
# Base 16: 0-9 and A-F
# Base 36: 0-9 and A-Z

import string

def is_valid_number(n, base):
    n = n.lower()
    # need to figure out the base values want to check in
    valid = []
    if base <=10:
        valid = valid + list(map(str, range(base)))
    else:
        letters = list(string.ascii_lowercase)
        letters = letters[:base-10] # don't need to remove 1 from base because goes up to and not including
        valid = valid + list(map(str, range(10))) + letters

    for char in n:
        if char not in valid: #issue is the type!
            print("here")
            return False

    return True 

if __name__ == '__main__':
    print(is_valid_number("10101", 2)) # True