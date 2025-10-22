import sys

input = sys.stdin.readline

length = int(input().rstrip())
points = []

for i in range(length):
    a, b = map(int, input().rstrip().split())
    points.append((a, b))

points.sort()

query = int(input().rstrip())
for _ in range(query):
    quest = float(input().rstrip())

    left, right = 0, len(points)-1

    while left < right:
        mid = (left+right) // 2

        if points[mid][0] <= quest:
            left = mid + 1
        else:
            right = mid

    idx = left
    # print(f"idx : {idx}")
    p1 = points[idx-1][1]
    p2 = points[idx][1]

    # print(f"p1 : {p1}, p2 : {p2}")
    if (p1 < p2): print(1)
    elif (p1 > p2): print(-1)
    else: print(0)


