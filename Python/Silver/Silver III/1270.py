import sys
# from decimal import Decimal

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    counts = dict()

    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    n = arr[0]
    arr = arr[1:]

    for a in arr:
        if not (a in counts): counts[a] = 0
        counts[a] += 1

    flag = 0
    for k, v in counts.items():
        # print(f"key : {k}, value : {v}")
        if v / n > 0.5:
            flag = 1
            print(k)
            break

    if not flag:
        print('SYJKGW')
            