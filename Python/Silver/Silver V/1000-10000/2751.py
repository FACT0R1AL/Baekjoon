import sys

arr = []
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()

for i in range(len(arr)):
    print(arr[i])
