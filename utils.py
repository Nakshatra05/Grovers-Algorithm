import numpy as np

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_factors(N):
    """Find factors of a number N."""
    factors = []
    for i in range(1, int(np.sqrt(N)) + 1):
        if N % i == 0:
            factors.append(i)
            if i != N // i:
                factors.append(N // i)
    factors.sort()
    return factors

def check_factorization(p, q, N):
    """Check if p and q are valid factors of N."""
    return p * q == N
