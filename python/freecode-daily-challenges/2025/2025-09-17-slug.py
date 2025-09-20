# Given a string, return a URL-friendly version of the string using the following constraints:

# All letters should be lowercase.
# All characters that are not letters, numbers, or spaces should be removed.
# All spaces should be replaced with the URL-encoded space code %20.
# Consecutive spaces should be replaced with a single %20.
# The returned string should not have leading or trailing %20.

def generate_slug(str):
    # lowercase
    # if not abc.. then remove
    # if " " then %20

    str = str.strip()
    slug = ""
    seen_whitespace = False
    for char in str:
        if char == " " and seen_whitespace != True:
            slug = slug + "%20"
            seen_whitespace = True
            continue
        seen_whitespace = False
        if not char.isalnum():
            continue
        
        char = char.lower()
        slug = slug + char

    return slug

    # Refactor to instead of iterating through every char,
    # first clean up the string, strip whitespace, remove with regex anything not alnum
    # replace all whitespace with %20?
    # or just add some "seen already" logic to be able to tell that we know it exists