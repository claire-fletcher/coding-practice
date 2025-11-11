import re

def count(s):
    # lowercase all so they are the same
    s = s.lower()

    # using regex, get a count of matches for single alpha chars
    letters = re.findall('[a-z]', s)

    # count with regex matches for a,e,i,o,u
    vowels = re.findall('[aeiou]', s)
    vowels_count = len(vowels)

    # consonants take vowel count from total alpha
    consonants_count = len(letters) - vowels_count

    return [vowels_count, consonants_count]