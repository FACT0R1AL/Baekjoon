fib = [1] * 10001
fib[0] = 0

for i in range(2, 10001):
    fib[i] = fib[i-1] + fib[i-2]

T = int(input())

for t in range(1, T+1):
    p, q = map(int, input().split())

    print(f"Case #{t}: {fib[p] % q}")