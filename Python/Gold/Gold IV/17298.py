n = int(input())

arr = list(map(int, input().split()))
top = 0
answer = [-1]
stack = [1000001]

def push(n):
    global stack, top
    stack.append(n)
    top += 1
def POP():
    global stack, top
    stack.pop()
    top -= 1

for i in range(n-1, -1, -1):
    flag = 1
    for j in range(top, -1, -1):
        if arr[i] < stack[j]:
            push(arr[i])
            if stack[j] == 1000001 and i != n-1: answer.append(-1)
            elif stack[j] == 1000001: answer.append(-1)
            else: answer.append(stack[j])
            flag = 0
            # print(f"stack : {stack}")
            break
        else:
            POP()
            # print(f"stack : {stack}")

    if (flag == 1): 
        # print(f"stack : {stack}")
        answer.append(-1)

for i in range(n, 0, -1):
    print(answer[i], end=" ")

# 3 5 2 7  5 7 7 -1
# stack [1000001] arr = 7
# stack [1000001, 7]
# answer [-1]
# stack [1000001, 7] arr = 2
# stack [1000001, 7, 2]
# answer [-1 7]
# stack [1000001, 7, 2] arr = 5
# stack [1000001, 7] arr = 5
# stack [1000001, 7, 5]
# answer = [-1 7 7]
# stack [1000001, 7, 5] arr = 3
# stack [1000001, 7, 5, 3]
# anser = [-1 7 7 5]

# 9 5 4 8
# 4 7 6 1
# 8 9