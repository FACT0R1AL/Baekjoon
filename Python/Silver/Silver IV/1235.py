import sys

input = sys.stdin.readline

n = int(input().rstrip())

arr = [input().rstrip() for _ in range(n)]

k = 1

while True:
    temp = []

    for string in arr:
        temp.append(string[-k:])
        
    if (len(set(temp)) == n): 
        break

    k += 1

print(k)