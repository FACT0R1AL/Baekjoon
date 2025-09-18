n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    hap = sum(arr[1:4])
    if (arr[3] - arr[1] >= 4): print("KIN")
    else: print(hap)