# Given a string of credit card numbers, return a masked version of it using the following constraints:

# The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
# Replace all numbers, except the last four, with an asterisk (*).
# Leave the remaining characters unchanged.
# For example, given "4012-8888-8888-1881" return "****-****-****-1881".

def mask(card):
    if " " in card:
        return f"**** **** **** {card[15:19]}"
    return f"****-****-****-{card[15:19]}"

# Note: this version works exactly to the specifications and is not particularly flexible.