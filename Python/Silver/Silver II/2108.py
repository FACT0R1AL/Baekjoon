import sys

length = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(length)]

arrsort = sorted(arr)

avg = round(sum(arr) / length)
center = arrsort[int(length/2)]
diff = abs(arrsort[0] - arrsort[-1])
high = 0

counts = dict()

for a in arr:
    if not (a in counts): counts[a] = 0
    counts[a] += 1

maxCount = max(counts.values())

highs = []
for k, v in counts.items():
    if v == maxCount:
        highs.append(k)

highs.sort()

print(avg)
print(center)

if (len(highs) == 1): print(highs[0])
else: print(highs[1])

print(diff)