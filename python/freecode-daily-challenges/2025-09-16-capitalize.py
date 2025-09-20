# Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

# All other characters should be preserved.
# Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).

def capitalize(paragraph):
    capitalized = ""

    end_found = True # start with true for first sentence
    for char in paragraph:

        # As soon as the end found is true and char is not a ?.!
        # then make it a capital and set end_found to false.
        # TODO: We can also break if upper already?
        if end_found and char != " ":
            capital = char.upper()
            # use the new character in the new paragraph
            capitalized = capitalized + capital
            end_found = False
            continue
        
        # Check if end character, set to true.
        # If multiple of the same then will 
        # set again, therefore still true
        if char in [".", "?", "!"]:
            end_found = True
        
        # add the current character if it doesn't get changed
        capitalized = capitalized + char
        

    return capitalized

    # Essentially adding each character to the new paragraph