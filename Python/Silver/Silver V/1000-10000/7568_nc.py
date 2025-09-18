n = int(input())

arr = []

for _ in range(n):
    arr.append(tuple(input().split()))

sortedArr = sorted(arr, key = lambda x:x[0], reverse = True)
print(arr, sortedArr)