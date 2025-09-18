from collections import deque

length = int(input())
arr = list(map(int, input().split()))

stack = [100000001]
answer = [0]

for i in range(length):
    flag = 1

# 6 9 5 7 4
# 0 0 2 2 4

# q [6]
# answer [0]
# q [6, 9]
# q [9]
# answer [0, 0]
# q [9 5]
# answer [0,0,2]
# q [9 5 7]
# q umm

# stack [100000001]
# answer [0]
# stack [100000001] arr = 6, top = 0
# stack [100000001, 6] top = 0
# answer [0]
# stack [100000001, 6] arr = 9, top = 1
# stack [100000001] arr = 9 top = 1
# answer [0, 0]
# stack [100000001, 9] arr = 5, top = 1
# stack [100000001, 9, 5] top = 1
# answer [0, 0, 2]

# stack 