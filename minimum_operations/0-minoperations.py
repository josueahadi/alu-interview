#!/usr/bin/python3

def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to get exactly n 'H' characters
    starting from a single 'H'. The allowed operations are:
    - Copy All: Copies all 'H' characters in the file.
    - Paste: Pastes the copied content into the file.
    
    The function uses a factorization approach to determine the minimum number of operations
    by finding the smallest divisors of n and calculating the total number of operations 
    required to achieve exactly n 'H' characters.
    
    Parameters:
    n (int): The target number of 'H' characters to achieve. Must be a positive integer.
    
    Returns:
    int: The minimum number of operations required to achieve n 'H' characters. 
         Returns 0 if n is less than or equal to 1, as it's not possible to achieve 
         more than one 'H' with the given operations.
      
    Example:
    >>> minOperations(4)
    4
    >>> minOperations(12)
    7
    """
    # If n is less than or equal to 1, it's impossible to reach more than one 'H'
    if n <= 1:
        return 0
    
    # Initialize the number of operations to 0
    operations = 0

    # Start with the smallest prime divisor
    divisor = 2

    # Loop until n is reduced to 1
    while n > 1:
        # Check if the current divisor can divide n
        while n % divisor == 0:
            # If it does, it means we need to perform 'divisor' number of operations
            # This is because to get n 'H' characters, we need to perform Copy All
            # and then paste 'divisor' times. Hence, each divisor contributes to the
            # number of operations.
            operations += divisor

            # Reduce n by dividing it by the current divisor
            n //= divisor

        # Move to the next potential divisor
        divisor += 1

    return operations
