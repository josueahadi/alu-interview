def minOperations(n: int) -> int:
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
