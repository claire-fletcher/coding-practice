import math

def infected(days):

    infected = 1
    for day in range(1, days+1):
        if day%3 == 0:
            infected = (infected*2)
            patch = math.ceil(infected*0.2)
            infected = infected - patch
        else:
            infected = infected*2

    return infected