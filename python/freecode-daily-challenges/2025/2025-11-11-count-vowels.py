import re

def count(s):
    # lowercase all so they are the same
    s = s.lower()

    # using regex, get a count of matches for single alpha chars
    letters_count = len(re.findall('[a-z]', s))

    # count with regex matches for a,e,i,o,u
    vowels_count = len(re.findall('[aeiou]', s))

    # consonants take vowel count from total alpha
    consonants_count = letters_count - vowels_count

    return [vowels_count, consonants_count]