import math


def prime_numbers(n):
    primes = [2]
    for i in range(2, n+1):
        can_divide = False
        for j in primes:
            if i % j == 0:
                can_divide = True
                break
        if not can_divide:
            primes.append(i)
    return primes


#  print(prime_numbers(13))


def prime_decomposition(n):
    centr = int(n // 2)
    primes = prime_numbers(centr)

    nn = n
    i = 0
    divides = []
    while i < len(primes):
        p = primes[i]
        if nn % p == 0:
            nn //= p
            divides.append(p)
        else:
            i += 1
    if len(divides) >= 1:
        return divides
    else:
        return [n]

print(prime_decomposition(12))
print(prime_decomposition(29))
print(prime_decomposition(2))
print(prime_decomposition(3))
print(prime_decomposition(28))



