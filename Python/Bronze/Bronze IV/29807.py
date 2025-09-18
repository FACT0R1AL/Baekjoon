n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(n-1, 5): arr.append(0)
    
if arr[0] > arr[2]: result += 508 * abs(arr[0]-arr[2])
else: result += 108 * abs(arr[0]-arr[2])
    
if arr[1] > arr[3]: result += 212 * abs(arr[1]-arr[3])
else: result += 305 * abs(arr[1]-arr[3])
    
if arr[4] > 0: result += 707 * arr[4]

print(result*4763)