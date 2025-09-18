erathos = [1] * 10001
erathos[0] = erathos[1] = 0

primes = []

for i in range(2, 10001):
    if (erathos[i]):
        primes.append(i)

        for j in range(i*i, 10001, i):
            erathos[j] = 0

primesSet = set(primes)
count = 0

a, b = map(int, input().split())

for i in range(a, b+1):
    length = 0
    n = i

    if n in primes: continue

    for prime in primes:
        if (prime * prime) > n: break

        while (n % prime == 0):
            n //= prime
            length += 1

    if n > 1: length += 1

    if (length in primesSet): count += 1

print(count)