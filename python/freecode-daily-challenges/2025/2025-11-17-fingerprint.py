import math

def is_match(fingerprint_a, fingerprint_b):

    if len(fingerprint_a) != len(fingerprint_b):
        return False
    
    margin = math.floor(0.1 * len(fingerprint_a))

    # compare the strings, in this case we assume order matters?
    # loop over them once. 
    diff = 0
    for x in range(len(fingerprint_a)):
        if fingerprint_a[x] != fingerprint_b[x]:
            diff = diff + 1
    
    if diff > margin:
        return False

    return True