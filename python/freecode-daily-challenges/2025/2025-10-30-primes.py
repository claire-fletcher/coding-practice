import math
def nth_prime(n):

    start = 2
    count = 0
    while True:
        # IF ALL, handy and new to me
        # also, use up to the square root due to maths as a prime is essentially checking that there are no two products other than 1, itself. so then we can use n = a*b and to get n from that they cant BOTH be greater than square root of n or it would be larger than n. Hence one must be less than, so if we can't find one then it is prime! 
        if all([start % i for i in range(2, int(math.sqrt(start)) + 1)]) != 0:
            count += 1
            if count == n:
                return start
        start += 1 

    return n

# Now we can estimate the upper bound of the prime number too and then potentially use a Sieve of Eratosthenes method to make this quicker?

# The Sieve of Eratosthenes efficiently finds all primes up to n by repeatedly marking multiples of each prime as non-prime, starting from 2. This avoids redundant checks and quickly filters out all composite numbers.