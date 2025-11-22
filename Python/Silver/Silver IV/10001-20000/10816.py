import sys

n = int(sys.stdin.readline())
have = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

count = dict()

arrset = set(arr)

for i in arr:
    count[i] = 0

for i in have:
    if i in arrset: count[i] += 1

for i in arr:
    print(count[i], end=' ')