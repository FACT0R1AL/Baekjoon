arr = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())

    for j in range(int((b-a+1)/2)):
        temp = arr[a+j-1]
        arr[a+j-1] = arr[b-j-1]
        arr[b-j-1] = temp
        
print(*arr)