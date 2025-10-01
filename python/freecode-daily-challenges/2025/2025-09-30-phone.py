# Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".

def format_number(number):
    return f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}"