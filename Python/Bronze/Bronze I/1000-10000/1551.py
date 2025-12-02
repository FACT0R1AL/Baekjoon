n, k = map(int, input().split())
arr = list(map(int, input().split(',')))
newArr = []

for i in range(1, k+1):
    for j in range(1, n-i+1):
        newArr.append(arr[j] - arr[j-1])

    for j in range(len(newArr)):
        arr[j] = newArr[j]

    arr.pop()
    newArr.clear()

for i in range(len(arr)):
    if i == len(arr)-1: print(f'{arr[i]}', end='')
    else: print(f'{arr[i]},', end='')