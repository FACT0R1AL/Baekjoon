import math

n = int(input())
n2 = int(input())

board = [[0 for i in range(n)] for j in range(n)]
posX, posY = n//2, n//2
n2posX, n2posY = 0, 0

if (n2 == 1):
    n2posX = posX
    n2posY = posY

i = 1
progress = 1

# first start (must be run)
board[posY][posX] = i
i += 1

while i <= n*n:
    # up 
    if (progress % 4 == 1):
        for j in range(progress//2 + 1 if progress%2 != 0 else progress//2):
            x = posX
            y = posY - 1

            board[y][x] = i
            posX = x
            posY = y
            
            if (i == n2):
                n2posX = posX
                n2posY = posY

            i += 1

            if (i > n*n): break
    
    # right
    elif (progress % 4 == 2):
        for j in range(progress//2 + 1 if progress%2 != 0 else progress//2):
            x = posX + 1
            y = posY

            board[y][x] = i
            posX = x
            posY = y

            if (i == n2):
                n2posX = posX
                n2posY = posY

            i += 1

            if (i > n*n): break

    # down
    elif (progress % 4 == 3):

        for j in range(progress//2 + 1 if progress%2 != 0 else progress//2):
            x = posX
            y = posY + 1

            board[y][x] = i
            posX = x
            posY = y
            
            if (i == n2):
                n2posX = posX
                n2posY = posY

            i += 1

            if (i > n*n): break

    # left
    elif (progress % 4 == 0):
        for j in range(progress//2 + 1 if progress%2 != 0 else progress//2):
            x = posX - 1
            y = posY

            board[y][x] = i
            posX = x
            posY = y
            
            if (i == n2):
                n2posX = posX
                n2posY = posY

            i += 1

            if (i > n*n): break

    progress += 1

for i in range(n):
    print(*board[i])

print(n2posY + 1, n2posX + 1)

# 49 26 27 28 29 30 31
# 48 25 10 11 12 13 32
# 47 24 09 02 03 14 33
# 46 23 08 01 04 15 34
# 45 22 07 06 05 16 35
# 44 21 20 19 18 17 36
# 43 42 41 40 39 38 37

# 1 up
# 1(2) right
# 2(3) down
# 2(4) left
# 3(5) up
# 3(6) right
# 4 down
# 4 left
# 5 up