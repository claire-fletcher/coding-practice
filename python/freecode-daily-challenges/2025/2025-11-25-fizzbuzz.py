# High readability but slow due to append
def fizz_buzz_readability(n):
    numbers = []
    for i in range(1,n+1):
        if i % 3==0 and i % 5==0:
            numbers.append("FizzBuzz")
        elif i % 3==0:
            numbers.append("Fizz")
        elif i % 5==0:
            numbers.append("Buzz")
        else:
            numbers.append(i)

    return numbers

# This version is more optimised but a balance between the two
def fizz_buzz_extendable(n):
    results = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0: output += "Fizz"
        if i % 5 == 0: output += "Buzz"
        
        # If output is empty, append i, else append output
        results.append(output or i) # short-cirtcuit evaluation, useful for when something may be empty so we can set a default or other value, usable elsewhere too.
    return results

# Note: Whenever there is a list being built, consider if we can use comprehensions so we have one less function. 
# Especially where we will be iterating anyway.
# But, this is less extendable where more rules might be added later.
def fizz_buzz_speed(n):
    return [
        "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i
        for i in range(1, n + 1)
    ]