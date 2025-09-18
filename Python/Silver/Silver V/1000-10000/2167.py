import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    hap = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())

    
    for i in range(x1-1, x2):
        hap += sum(arr[i][y1-1:y2])

    print(hap)