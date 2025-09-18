arr = [0 for _ in range(10002)]
arr[1] = 1

n = int(input())

for i in range(n):
    arr[i+2] = arr[i+1] + arr[i]

print(arr[n])