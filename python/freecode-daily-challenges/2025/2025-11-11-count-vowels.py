import re

def count_regex(s):
    # lowercase all so they are the same
    s = s.lower()

    # using regex, get a count of matches for single alpha chars
    letters_count = len(re.findall('[a-z]', s))

    # count with regex matches for a,e,i,o,u
    vowels_count = len(re.findall('[aeiou]', s))

    # consonants take vowel count from total alpha
    consonants_count = letters_count - vowels_count

    return [vowels_count, consonants_count]

vowels = 'aeiou'

def count(s):
    s = s.lower()

    # Simplified version that uses sum and generator expression as regex creates lists
    vowels_count = sum(1 for char in s if char in vowels)
    consonants_count = sum(1 for char in s if char.isalpha() and char not in vowels)

    return [vowels_count, consonants_count]
