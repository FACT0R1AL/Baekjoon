import sys

length = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
n = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(length)] for _ in range(length)]

for i in range(length):
    dp[i][i] = 1

for i in range(length-1):
    if arr[i] == arr[i+1]: dp[i][i+1] = 1

for l in range(3, length+1):
    for i in range(length - l + 1):
        j = l + i - 1
        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

for i in range(n):
    flag = 1
    s, e = map(int, sys.stdin.readline().rstrip().split())
    if (dp[s-1][e-1] == 1): print(1)
    else: print(0)