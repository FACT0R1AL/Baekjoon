n, m = map(int, input().split())

arr = set(input() for _ in range(n))
have = list(input() for _ in range(m))

count = 0

for i in have:
    if (i in arr): count += 1

print(count)