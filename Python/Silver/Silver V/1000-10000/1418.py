n = int(input())
k = int(input())

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

    if n == 1: return [1]
    if n in primes: return [n]

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

count = 0

for i in range(1, n+1):
    factor = prime_factor(i)
    maxF = max(factor)

    if (maxF <= k): 
        count += 1
        
        #print(i)

print(count)