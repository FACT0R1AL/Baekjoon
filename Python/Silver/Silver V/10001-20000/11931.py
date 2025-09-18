import sys

length = int(sys.stdin.readline().rstrip())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(length)]

arr.sort(reverse=True)

for a in arr:
    print(a)