# Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

# The string can contain any characters.
# The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
# If there's an odd number of characters in the string, ignore the center character.

import math

def is_balanced(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s.lower() # turn all to lower for ease

    i = 0
    j = math.ceil(len(s)/2)
    count_left = 0
    count_right = 0
    while j<len(s):
        if s[i] in vowels:
            count_left += 1
        if s[j] in vowels:
            count_right += 1
        i += 1
        j += 1

    return count_left == count_right

    # OR instead of splitting, we could do a two pointers thing where we 
    # count every time a char is in the vowels until we get to the end?
    # then to ignore the middle we can do 
    # 7/2 = 3.5 so we want to do i=0, j=4, until j<len, need to add the ceil. 