N = 150000
P = [0] * (N + 1)  # 최종 순열
cur = N

intervals = [(1, N)]

while intervals:
    l, r = intervals.pop(0)
    mid = (l + r) // 2
    P[mid] = cur
    cur -= 1

    left = (l, mid - 1)
    
    if left[0] <= left[1]:
        if left[1] - left[0] > (intervals[0][1] - intervals[0][0] if intervals else -1):
            intervals.insert(0, left)
        else:
            intervals.append(left)

    right = (mid + 1, r)

    if right[0] <= right[1]:
        if right[1] - right[0] > (intervals[0][1] - intervals[0][0] if intervals else -1):
            intervals.insert(0, right)
        else:
            intervals.append(right)

perm = P[1:]
print(*perm)
