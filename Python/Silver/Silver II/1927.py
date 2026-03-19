import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())

heap = []

for _ in range(N):
    x = int(input().rstrip())

    if (x == 0):
        if (heap == []):
            print(0)

        else:
            popped = heapq.heappop(heap)
            print(popped)

    else:
        heapq.heappush(heap, x)