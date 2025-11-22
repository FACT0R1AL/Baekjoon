WB = ['WBWBWBWB', 'BWBWBWBW'] * 4
BW = ['BWBWBWBW', 'WBWBWBWB'] * 4

H, W = map(int, input().split())

arr = [input() for _ in range(H)]
minCount = H*W

for i in range(0, H-7):
    for j in range(0, W-7):
        countWB = 0
        countBW = 0

        for k in range(i, 8+i):
            for l in range(j, 8+j):
                if (arr[k][l] != WB[k-i][l-j]): countWB += 1
                if (arr[k][l] != BW[k-i][l-j]): countBW += 1
        
        minCount = min(minCount, min(countWB, countBW))

print(minCount)