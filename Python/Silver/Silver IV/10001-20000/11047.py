n, k = map(int, input().split())
types = []
count = 0

for i in range(n):
    types.append(int(input()))

types.reverse()

for i in range(n):
    count += k // types[i]
    k %= types[i]
    # print(count, k)

print(count)