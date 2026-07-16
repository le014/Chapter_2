from math import sqrt

def isprime(n):
    if n < 2:
        return False
    for m in range(2, int(sqrt(n)) + 1):
        if n % m == 0:
            return False
    return True
