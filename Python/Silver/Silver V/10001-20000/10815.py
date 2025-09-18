import sys

n = int(sys.stdin.readline())
have = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in arr:
    print(1 if i in have else 0, end=' ')