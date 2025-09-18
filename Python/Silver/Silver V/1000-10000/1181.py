n = int(input())
arr = []

for i in range(n):
    temp = input()
    arr.append((temp, len(temp)))

arr = set(arr)
arr = list(arr)
arr.sort(key = lambda x:(x[1], x[0]))

for i in range(len(arr)):
    print(arr[i][0])