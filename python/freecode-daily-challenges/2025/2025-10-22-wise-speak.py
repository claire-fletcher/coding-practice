import re


def wise_speak(sentence):

    cleaned = re.sub(r'[^\w\s]', '', sentence)
    cleaned = cleaned.casefold()
    split = cleaned.split()

    length = len(split)

    index = 0
    for word in split:
        if word in ["have", "must", "are", "will", "can"]:
            start = " ".join(split[index+1:length])
            start = start.capitalize()
            end = " ".join(split[0:index+1])
            return f"{start}, {end}{sentence[-1]}"
        index = index + 1

    return "No Key Word"

print(wise_speak("You must learn to code."))