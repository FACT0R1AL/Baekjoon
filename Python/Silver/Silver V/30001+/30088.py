import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

arr.sort(key = lambda x: sum(x[1:]))

time = []
fullTime = 0

for i in range(n):
    time.append(sum(arr[i][1:]))

for i in range(n):
    fullTime += sum(time[:i+1])

    # print(sum(time[:i+1]), fullTime)

print(fullTime)