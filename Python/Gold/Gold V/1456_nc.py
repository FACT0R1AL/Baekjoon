erathos = [1] * 10000001
erathos[0] = erathos[1] = 0
primes = []
almost_primes = []

for i in range(2, 10000001):
    if (erathos[i]):
        primes.append(i)

        for j in range(i*i, 10000001, i):
            erathos[j] = 0

for i in range(len(primes)):
    idx = 2
    while pow(primes[i], idx) <= pow(10, 14):
        almost_primes.append(pow(primes[i], idx))
        idx += 1

almost_primes.sort()

a, b = map(int, input().split())

left, right = 0, len(almost_primes)

while left <= right:
    mid = (left + right) // 2
    if almost_primes[mid] < a:
        left = mid + 1
    else:
        right = mid - 1

idx = mid
count = 0

while idx < len(almost_primes) and almost_primes[idx] <= b:
    # print(almost_primes[idx])

    if (almost_primes[idx] >= a): count += 1
    idx += 1

print(count)