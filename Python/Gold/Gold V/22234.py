import sys
from collections import deque

input = sys.stdin.readline

N, T, w = map(int, input().rstrip().split())

# id, time, arrival
customers = deque()

for i in range(N):
    px, tx = map(int, input().rstrip().split())
    customers.append(deque([px, tx, 0]))

M = int(input().rstrip())

for i in range(M):
    px, tx, cx = map(int, input().rstrip().split())
    customers.append(deque([px, tx, cx]))

customers = sorted(customers, key = lambda x : x[2])
length = len(customers)

timer = 0
flag = False

while True:
    if (customers[0][2] > timer):
        temp = customers.pop(0)
        customers.append(temp)

    else:
        if (customers[0][1] <= T):
            for _ in range(customers[0][1]):
                print(customers[0][0])
                timer += 1
                customers[0][2] += 1

                if (timer >= w):
                    flag = True
                    break

            del(customers[0])
            length -= 1

        else:
            for _ in range(T):
                print(customers[0][0])
                timer += 1
                customers[0][2] += 1

                if (timer >= w):
                    flag = True
                    break

            customers[0][1] -= T

            temp = customers.pop(0)
            customers.append(temp)

            # customers = sorted(customers, key = lambda x : x[2])

    # print(customers)

    if (length <= 0 or timer == w or flag == True): break

# 3 1 10
# 1 2
# 2 3
# 3 1
# 2 
# 4 1 1
# 5 3 2

# 1
# 2
# 3
# 4
# 1
# 5
# 2
# 5
# 2
# 5