dp = [0] * 5002

dp[:2] = [-1, -1, -1]
dp[3] = 1
dp[4] = 0
dp[5] = 1
dp[6] = 2
dp[7] = 0
dp[8] = 2

for i in range(9, 5001):
    if (dp[i-3] != 0 and dp[i-5] != 0):
        dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
    else:
        dp[i] = max(dp[i-3] + 1, dp[i-5] + 1)

n = int(input())

if (dp[n] == 0): print(-1)
else: print(dp[n])