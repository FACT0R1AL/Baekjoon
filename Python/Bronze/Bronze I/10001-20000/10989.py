import sys

cnt = [0 for _ in range(10002)]
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    cnt[int(sys.stdin.readline().rstrip())] += 1

for i in range(1, 10002):
    if (cnt[i]):
        for j in range(cnt[i]): print(i)