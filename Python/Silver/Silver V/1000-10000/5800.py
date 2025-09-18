import sys

T = int(input())

for _ in range(T):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    n = arr[0]
    arr = arr[1:]

    arr.sort()
    diff = 0

    for i in range(1, len(arr)):
        if (diff < arr[i] - arr[i-1]):
            diff = arr[i] - arr[i-1]

    print(f"Class {_+1}")
    print(f"Max {arr[-1]}, Min {arr[0]}, Largest gap {diff}")