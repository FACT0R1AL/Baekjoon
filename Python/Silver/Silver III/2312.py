erathos = [1] * 100001
erathos[0] = erathos[1] = 0
primes = []

for i in range(2, 100001):
    if (erathos[i]):
        primes.append(i)
        for j in range(i*i, 100001, i):
            erathos[j] = 0

T = int(input())

for _ in range(T):
    n = int(input())

    factors = dict()

    while n != 1:
        for p in primes:
            if (n % p == 0):
                n //= p

                isKey = factors.get(p)
                if (isKey == None): 
                    factors[p] = 1
                    break
                else: 
                    factors[p] += 1
                    break
    
    for k, v in factors.items():
        print(k, v)
