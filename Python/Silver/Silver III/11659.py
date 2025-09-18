import sys

input = sys.stdin.readline

length, query = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

hap = [0] * (length+1)

for i in range(length):
    hap[i+1] = hap[i] + arr[i]

for _ in range(query):
    a, b = map(int, input().rstrip().split())

    print(hap[b] - hap[a-1])