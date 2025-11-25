erathos = [1] * 100001
erathos[0] = erathos[1] = 0
primes = []

for i in range(2, 100001):
    if (erathos[i]):
        primes.append(i)

        for j in range(i*i, 100001, i):
            erathos[j] = 0

def prime_factor(n):
    factors = []

    if n == 1: return 0
    if milLaPrime(n): return "prime"

    while n != 1:
        for p in primes:
            if p * p > n:
                factors.append(n)
                return factors

            if (n % p == 0):
                n //= p
                factors.append(p)
                break

    return factors

def fastPow(base, exp, mod):
    result = 1
    base %= mod

    while exp > 0:
        if (exp%2):
            result = (result*base) % mod
        
        base = (base*base) % mod
        exp //= 2

    return result

def milLaPrime(n):
    tempA = [2, 7, 61]
    s = 0
    p = n - 1

    while p % 2 == 0:
        p //= 2
        s += 1
    d = p

    for a in tempA:
        if a % n == 0:
            continue
        x = fastPow(a, d, n)

        if x == 1 or x == n - 1: continue

        flag = False
        for _ in range(s - 1):
            x = fastPow(x, 2, n)
            if x == n - 1:
                flag = True
                break

        if not flag: return 0

    return 1

t = int(input())

for _ in range(t):
    n = int(input())

    factor = prime_factor(n)

    if (factor == "prime"): print(f"{n}: prime")
    else: 
        print(f"{n}: ", end = '')
        print(*factor)
