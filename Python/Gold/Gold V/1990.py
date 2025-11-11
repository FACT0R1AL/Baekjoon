erathos = [1] * 10000000
erathos[0] = erathos[1] = 0

primes = []

for i in range(2, 10000000):
    if (erathos[i]):
        primes.append(i)

        for j in range(i*i, 10000000, i):
            erathos[j] = 0

def palindrome(n):
    return str(n) == str(n)[::-1]

a, b = map(int, input().split())

left, right = 0, len(primes)-1

while left < right:
    mid = (left+right) // 2

    if primes[mid] <= a:
        left = mid + 1
    else:
        right = mid - 1

# print(mid, primes[mid])
idx = left

while primes[idx] <= b and idx < len(primes):
    if (primes[idx] >= 10000000): break
    if palindrome(primes[idx]):
        print(primes[idx])

    idx += 1

print(-1)