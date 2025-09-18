H, W = map(int, input().split())

arr = []
rank = [0] * 9
rankCount = 1
for i in range(H):
    temp = list(input())
    arr.append(temp)

for i in range(W-1):
    flag = 0
    for j in range(H):
        if (arr[j] != []): 
            arr[j].pop()

            if (arr[j][-1].isdigit()):
                rank[int(arr[j][-1]) - 1] = rankCount
                flag = 1
                arr[j].clear()

    if (flag): rankCount += 1

for i in range(len(rank)):
    print(rank[i])