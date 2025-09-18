while True:
    h, w = map(int, input().split())
    arr = []
    new_arr = []

    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    if (h == 0 and w == 0): break

    for i in range(h):
        arr.append(input())

    for i in range(h):
        for j in range(w):
            cnt = 0

            if (arr[i][j] == '.'):
                for x, y in zip(dx, dy):
                    nx, ny = i + x, j + y

                    if (nx >= 0 and nx < w and ny >= 0 and ny < h):
                        if (arr[ny][nx] == '*'):
                            cnt += 1
                
                new_arr.append(str(cnt))

            else:
                new_arr.append('*')

    print(new_arr)

    for i in range(h):
        for j in range(w):
            print(new_arr[i*h+j-i], end='')
        
        print('')