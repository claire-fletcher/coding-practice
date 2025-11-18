import math

def one_hundred(chars):

    repeat = math.ceil(100/len(chars))
    new = chars
    for x in range(repeat):
        new = new + chars

    return new[0:100]

# First attempt and very slow, just the literal concept.
# Reduced slightly by figuring out a repeat amount.

# Second attempt which was my first approach using something I previously learnt!
# This approach is much more efficient as we build the string instead of looping.

import math

def one_hundred(chars):

    new = chars*100 #This ensures it is always above 100 no matter what

    return new[0:100]