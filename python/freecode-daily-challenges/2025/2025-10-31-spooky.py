def spookify(boo):
    # swap all _
    boo = boo.replace("_", "~")
    boo = boo.replace("-", "~")

    # Capitalise every other LETTER, also LOWERCASE the others
    letter_capitalized = False
    new_boo = ""
    for char in boo:
        # Case that nothing needs to change
        if not char.isalpha():
            new_boo = new_boo + char # use f string?    
        elif letter_capitalized:
            new_boo = new_boo + char.lower() # use f string?
            letter_capitalized = False
        else:
            # Case where capitalization is needed
            new_boo = new_boo + char.capitalize()
            letter_capitalized = True

    return new_boo

if __name__ == "__main__":
    test_boo = "c_a-n_d-y_-b-o_w_l"
    print(spookify(test_boo))
