perfectBoard = [['A','B','C','D'],
                ['E','F','G','H'],
                ['I','J','K','L'],
                ['M','N','O','.']]

board = []

distance = 0

for i in range(4):
    board.append(input())

for i in range(4):
    for j in range(4):
        if (board[i][j] != perfectBoard[i][j] and board[i][j] != '.'):
            for k in range(4):
                for l in range(4):
                    if (board[i][j] == perfectBoard[k][l]): distance += abs(k-i) + abs(l-j)

print(distance)