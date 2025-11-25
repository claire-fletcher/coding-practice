def is_valid_message(message, validation):
    words = message.lower().split()
    validation = validation.lower()

    if len(words) != len(validation):
        return False

    # words[0][0] = validation[0]
    # words[1][0] = validation[1]
    # words[2][0] = validation[2] etc
    for x in range(0, len(validation)):
        if words[x][0] != validation[x]:
            return False

    return True