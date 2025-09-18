erathos = [1] * 10000001
erathos[0] = erathos[1] = 0

primes = []

for i in range(2, 10000001):
    if (erathos[i]):
        primes.append(str(i))
        
        for j in range(i*i, 10000001, i):
            erathos[j] = 0

N = int(input())

for prime in primes:
    if int(prime) < N: continue

    flag = 0

    for i in range(len(prime)):
        if (prime[i] != prime[len(prime) - i - 1]):
            flag = 1
            break

    if (flag == 0):
        print(int(prime))
        break
