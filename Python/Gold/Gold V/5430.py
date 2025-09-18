import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    cmd = sys.stdin.readline().rstrip()
    length = int(sys.stdin.readline().rstrip())

    temp = sys.stdin.readline().rstrip()
    temp = temp.strip('[]')
    if (temp == ''):
        arr = deque()
    else:
        arr = deque(map(int, temp.split(',')))

    flag = 1
    direction = 1

    for c in cmd:
        if c == 'R': direction *= -1
        elif c == 'D': 
            if (len(arr) > 0): 
                if (direction == 1): arr.popleft()
                else: arr.pop()
            else: 
                flag = 0
                print('error')
                break

    if flag:
        if direction == -1:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")