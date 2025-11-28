erathos = [1] * 50001
erathos[0] = erathos[1] = 0
primes = []

for i in range(2, 50001):
    if (erathos[i]):
        primes.append(i)
        
        for j in range(i*i, 50001, i):
            erathos[j] = 0

T = int(input())

for _ in range(T):
    k = int(input())

    length = len(primes)

    pq = 0
    minDiff = 100001
    p, q = 0, 0
    for i in range(length):
        for j in range(i+1, length):
            pq = primes[i] * primes[j]

            if (k <= pq):
                diff = pq - k
                if (diff < minDiff):
                    minDiff = diff
                    p, q = primes[i], primes[j]

    print(k + minDiff)
    print(f"{p} * {q} = {p*q}")