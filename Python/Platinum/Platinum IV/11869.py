n = int(input())

arr = list(map(int, input().split()))

xor = arr[0]

for i in range(1, n):
    xor ^= arr[i]

if (xor): print('koosaga')
else: print('cubelover')