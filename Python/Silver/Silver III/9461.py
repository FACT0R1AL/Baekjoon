dp = []

dp.append(1)
dp.append(1)
dp.append(1)
dp.append(2)
dp.append(2)

for i in range(5, 101):
    dp.append(dp[i-1] + dp[i-5])

T = int(input())

for _ in range(T):
    n = int(input())

    print(dp[n-1])