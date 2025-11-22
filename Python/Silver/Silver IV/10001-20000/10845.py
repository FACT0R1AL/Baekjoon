from collections import deque
import sys

q = int(sys.stdin.readline().rstrip())
arr = deque()

for i in range(q):
    cmd = sys.stdin.readline().rstrip()

    if cmd[:4] == 'push':
        arr.append(cmd[5:])

    elif cmd == 'front':
        if (len(arr) != 0): print(arr[0])
        else: print(-1)

    elif cmd == 'back':
        if (len(arr) != 0): print(arr[-1])
        else: print(-1)

    elif cmd == 'empty':
        if (len(arr) != 0): print(0)
        else: print(1)

    elif cmd == 'size':
        print(len(arr))

    elif cmd == 'pop':
       if (len(arr) != 0): print(arr.popleft())
       else: print(-1)