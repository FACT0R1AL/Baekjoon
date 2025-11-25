erathos = [1] * 10000001
erathos[0] = erathos[1] = 0

primes = []

for i in range(2, 10000001):
    if (erathos[i]):
        primes.append(i)

        for j in range(i*i, 10000001, i):
            erathos[j] = 0

def palindrome(n):
    return str(n) == str(n)[::-1]

a, b = map(int, input().split())

left, right = 0, len(primes)-1

while left <= right:
    mid = (left + right) // 2
    if primes[mid] < a:
        left = mid + 1
    else:
        right = mid - 1

# print(mid, primes[mid])
idx = left

while idx < len(primes) and primes[idx] <= b:
    if (primes[idx] >= 10000000): break
    if palindrome(primes[idx]):
        print(primes[idx])

    idx += 1

    # print(idx, len(primes))

print(-1)