import sys

input = sys.stdin.readline

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
        if a % n == 0: continue
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

count = 0

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    
    if (milLaPrime(2*n+1)): count += 1

print(count)