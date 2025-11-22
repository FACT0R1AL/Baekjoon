n = int(input())

arr = [1]

i = n-1
idx = 0

while i > 0:
    arr.append(arr[idx] + i * pow(-1, idx))

    i -= 1
    idx += 1

print(*arr)