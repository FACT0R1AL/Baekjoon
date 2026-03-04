import sys

input = sys.stdin.readline

def check(a, d, n, s):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
        
    for _ in range(s - 1):
        x = pow(x, 2, n)

        if x == n - 1:
            return True
            
    return False

def isPrime(n):
    if n < 2:
        return False

    testPrimes = [2, 3, 5, 7, 11]

    # n-1 = d * 2^s 분해
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in testPrimes:
        if a % n == 0:
            continue
        if not check(a, d, n, s):
            return False

    return True
count = 0

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    
    if (isPrime(2*n+1)): count += 1

print(count)