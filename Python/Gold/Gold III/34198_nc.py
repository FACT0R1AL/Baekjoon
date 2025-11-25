import sys
from collections import deque

input = sys.stdin.readline

length = int(input().rstrip())
queue = deque(map(int, input().rstrip().split()))

query = int(input())
popped = []

for _ in range(query):
    cmd = input().rstrip().split()

    if (cmd[0] == 'SF'):
        queue.rotate(-1)
        # print(f"SF query : {queue}  {popped}")

    elif (cmd[0] == 'SL'):
        queue.rotate(1)
        # print(f"SL query : {queue}  {popped}")

    elif (cmd[0] == 'SM'):
        n = int(cmd[1])
        idx = queue.index(n)

        temp = list(queue)
        
        queue = deque(temp[idx+1:] + [n] + temp[:idx])

        # print(f"SM query : {queue}  {popped}")

    elif (cmd[0] == 'PF'):
        popped.append(queue.popleft())
        # print(f"PF query : {queue}  {popped}")

    elif (cmd[0] == 'PL'):
        popped.append(queue.pop())
        # print(f"PL query : {queue}  {popped}")

    elif (cmd[0] == 'PM'):
        n = int(cmd[1])
        idx = queue.index(n)

        popped.append(queue[idx])
        del queue[idx]

        # print(f"PM query : {queue}  {popped}")

print(*popped)