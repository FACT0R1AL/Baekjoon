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

def binary_search(arr, target, mode):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if mode == 0:
            if arr[mid] <= target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        else:
            if arr[mid] >= target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

    if result == -1:
        return 0 if mode == 0 else len(arr)

    return result

a, b = map(int, input().split())

idxLeft = binary_search(almost_primes, a, 0)
idxRight = binary_search(almost_primes, b, 1)

print(idxRight, len(almost_primes))
count = len(almost_primes[idxLeft+1:idxRight])

if (almost_primes[idxLeft] == a): count += 1
if (idxRight != len(almost_primes) and almost_primes[idxRight] == b): 
    if (a != b): count += 1
if (a == 1): count += 1
print(almost_primes[idxLeft+1:idxRight])
print(count)