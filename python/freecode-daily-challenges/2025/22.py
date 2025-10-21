import re

def digits_or_letters(s):
    numbers = len(re.findall('[0-9]', s))
    letters = len(re.findall('[a-zA-Z]', s))

    if numbers > letters:
        return "digits"
    if letters > numbers:
        return "letters"

    return "tie"