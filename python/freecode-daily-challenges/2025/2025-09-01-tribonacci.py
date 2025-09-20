# The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

# Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

# Your function should handle sequences of any length greater than or equal to zero.
# If the length is zero, return an empty array.
# Note that the starting numbers are part of the sequence.

# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-01

def tribonacci_sequence(start_sequence, length):

    # Case where length of the sequence is part of the start
    if length <3:
        return start_sequence[:length]

    # Case where we continue to extend the sequence
    for i in range(length-3):
        new = start_sequence[i] + start_sequence[i+1] + start_sequence[i+2]
        start_sequence.append(new)
    
    return start_sequence

    # O notation is n where n is the length.