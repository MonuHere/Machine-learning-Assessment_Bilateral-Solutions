def prime_factorization(n):
    factors = []
    # Check the number of 2s that divide n
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 0:
        factors.append((2, count))

    # Check for odd factors starting from 3
    factor = 3
    while factor * factor <= n:
        count = 0
        while n % factor == 0:
            n //= factor
            count += 1
        if count > 0:
            factors.append((factor, count))
        factor += 2

    # If n is a prime number greater than 2
    if n > 2:
        factors.append((n, 1))

    return factors

# Example usage:
print(prime_factorization(60))  # Output: [(2, 2), (3, 1), (5, 1)]
