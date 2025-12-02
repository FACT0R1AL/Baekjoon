H, W = map(int, input().split())
emptyC = []  # 열
emptyR = []  # 행

arr = []
count = 0

for i in range(H):
    temp = input()
    arr.append(temp)

for i in range(W):
    flag = 0
    for j in range(H):
        if (arr[j][i] == 'X'):
            flag = 1
            break

    if (flag == 0): emptyC.append(i+1)

for i in range(H):
    flag = 0
    for j in range(W):
        if (arr[i][j] == 'X'):
            flag = 1
            break

    if (flag == 0): emptyR.append(i+1)

while (emptyC != [] or emptyR != []):
    if (emptyC != []): emptyC.pop()
    if (emptyR != []): emptyR.pop()

    count += 1

print(count)