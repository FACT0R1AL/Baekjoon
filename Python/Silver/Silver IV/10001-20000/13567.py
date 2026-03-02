M, n = map(int, input().split())

x, y = 0, 0
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
idx = 0
flag = True

for _ in range(n):
    command, cx = input().split()
    cx = int(cx)

    if (command == "MOVE"):
        x += direction[idx][0] * cx
        y += direction[idx][1] * cx

    elif (command == "TURN"):
        if (cx == 0):
            idx -= 1
        else:
            idx += 1

    if (idx <= -4):
        idx = 0
    elif (idx >= 4):
        idx = 0
    
    # print(x, y, direction[idx], M)

    if (x > M or y > M or x < 0 or y < 0):
        flag = False
        print(-1)
        break

if (flag):
    print(x, y)