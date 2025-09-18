N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

FOX = 'FOX'
directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
count = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] != FOX[0]: continue

        for dx, dy in directions:
            x, y = i, j
            k = 0

            while k < 3:
                if not (0 <= x < N and 0 <= y < M): break
                if (arr[x][y] != FOX[k]): break

                x += dx
                y += dy
                k += 1

            if (k == 3): count += 1

print(count)