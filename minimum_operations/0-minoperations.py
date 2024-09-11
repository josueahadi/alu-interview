#!/usr/bin/python3
"""
Minimum operations to reach n characters
"""


def minOperations(n):
    """
    Calculates the minimum operations to reach n characters

    Args:
        n (int): The number of characters to reach

    Returns:
        int: The minimum operations to reach n characters
    """
    # Edge cases [0, 1]
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n = n // divisor
            operations += divisor
        else:
            divisor += 1
    return operations
