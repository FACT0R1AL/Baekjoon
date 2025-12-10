length = int(input())
string = input()
price = list(map(int, input().split()))

idx = 0
UOSPC = {'U' : 0,
         'O' : 1,
         'S' : 2,
         'P' : 3,
         'C' : 4}

dp = [1000000001] * 5

for i in range(length):
    if (dp[UOSPC[string[i]]] > price[i]):
        dp[UOSPC[string[i]]] = price[i]

if (1000000001 in dp):
    print(-1)
else:
    print(sum(dp))