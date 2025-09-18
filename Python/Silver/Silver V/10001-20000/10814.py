n = int(input())
arr = []

for i in range(n):
    num, string = input().split()
    num = int(num)

    arr.append((num, string))

arr.sort(key = lambda x:x[0])

for a, b in arr:
    print(a, b)