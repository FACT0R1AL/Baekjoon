import sys

input = sys.stdin.readline

stack = []

n = int(input().rstrip())

for _ in range(n):
    cmd, *n = map(int, input().rstrip().split())

    if (cmd == 1):
        stack.append(n[0])
    
    elif (cmd == 2):
        if (len(stack) > 0): print(stack.pop())
        else: print(-1)
    
    elif (cmd == 3):
        print(len(stack))

    elif (cmd == 4):
        if (len(stack) > 0): print(0)
        else: print(1)

    elif (cmd == 5):
        if (len(stack) > 0): print(stack[-1])
        else: print(-1)
