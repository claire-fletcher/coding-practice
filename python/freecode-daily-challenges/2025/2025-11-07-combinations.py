import math
def combinations(cards):
    # n choose r, can use math function
    return math.comb(52, cards)

def combinations_without_math(cards):
    # n choose r = n! / (r! * (n - r)!)
    n = 52
    r = cards

    # TODO: implement 

    return 0
    