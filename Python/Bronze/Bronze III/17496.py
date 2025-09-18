n, t, p, c = map(int, input().split())

cnt = 0
check = 1

while (check < n):
    check += t
    cnt += p

if (check > n): print(c * cnt - c*p)
else: print(c*cnt)