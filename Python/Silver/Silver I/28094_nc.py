from itertools import permutations

T = int(input())

for _ in range(T):
    V, A, B = [], [], []
    n, m = map(int, input().split())
    
    for i in range(m):
        v, a, b = map(int, input().split())

        V.append(v)
        A.append(a)
        B.append(b)

    for i in permutations([i for i in range(1, n+1)], n):
        arr = list(i)
            