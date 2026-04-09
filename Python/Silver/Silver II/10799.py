from collections import deque

string = input()

stack = []
cnt = 0

for i in range(len(string)):
    if (string[i] == '('):
        stack.append('(')

    else:
        stack.pop()

        if (string[i-1] == '('):
            cnt += len(stack)

        else:
            cnt += 1
        
print(cnt)

# ()(((()())(())()))(())