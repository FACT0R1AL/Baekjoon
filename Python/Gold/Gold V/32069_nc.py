import sys

length, n, k = map(int, sys.stdin.readline().split())
brightness = [-1 for _ in range(length+1)]
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    brightness[arr[i]] = 0

