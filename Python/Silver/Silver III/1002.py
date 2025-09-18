import math

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

    if (x1 == x2 and y1 == y2 and r1 == r2): print(-1)
    elif (abs(r1-r2) < distance < abs(r1+r2)): print(2)
    elif (distance == abs(r1-r2) or distance == abs(r1+r2)): print(1)
    else: print(0)