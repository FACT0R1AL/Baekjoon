import sys

input = sys.stdin.readline

erathos = [1] * 10000001
erathos[0] = erathos[1] = 0

for i in range(2, 250000):
    if (erathos[i]):
        
        for j in range(i*i, 250000, i):
            erathos[j] = 0

while True:
    n = int(input().rstrip())

    if (n == 0): break

    count = 0

    for i in range(n+1, 2*n+1):
        if (erathos[i]): count += 1

    print(count)