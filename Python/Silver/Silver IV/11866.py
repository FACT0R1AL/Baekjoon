from collections import deque

q = deque()
arr = []

n, k = map(int, input().split())

for i in range(1, n+1):
    q.append(i)

while (len(q) >= 1):
    q.rotate(-(k-1))
    arr.append(q.popleft())


print('<', end='')
for i in arr:
    if (i != arr[-1]): print(i, end=', ')
    else: print(i, end='')
print('>', end='')