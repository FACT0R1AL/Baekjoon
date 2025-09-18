n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
count = [0 for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        same = False
        for k in range(5):
            if arr[i][k] == arr[j][k]:
                same = True
                break
        if same:
            count[i] += 1
            count[j] += 1


# print(*count)
print(count.index(max(count)) + 1)