#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factor n by its prime factors
    while n > 1:
        while n % divisor == 0:
            operations += divisor  # Increment operations by the current divisor
            n //= divisor          # Divide n by the divisor
        divisor += 1              # Move to the next potential prime factor

    return operations

