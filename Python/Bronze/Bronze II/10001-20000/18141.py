n = int(input())

arr = list(map(int, input().split()))
length = len(arr)

flag = 1

for i in range(length):
    for j in range(length):
        for k in range(length):
            if (i != j and j != k and i != k):
                if (((arr[i]-arr[j]) / arr[k]) - int((arr[i]-arr[j]) / arr[k]) != 0):
                    flag = 0
                    break

if (flag): print("yes")
else: print("no")