#!/usr/bin/python3
"""
Minimum operations
"""
def minOperations(n):

    if n <= 1:
        return 0

    # Initialize the operations count
    operations = 0

    # Start dividing n by its smallest prime factors
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

