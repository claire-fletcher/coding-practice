def convert(heading):

    split = heading.strip().split(" ")
    
    # Ensure contains a hash
    if "#" not in split[0]:
        return "Invalid format"
    # Ensure a space
    if split[0] != len(split[0]) * "#":
        return "Invalid format"
    # Ensure the length of #
    if len(split[0]) > 6:
        return "Invalid format"
    h_tag = len(split[0])

    text = " ".join(split[1:len(split)]).strip()
    

    return f"<h{h_tag}>{text}</h{h_tag}>"