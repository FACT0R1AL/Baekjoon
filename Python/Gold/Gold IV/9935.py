word = input()
boom = input()

lengthWord = len(word)
lengthBoom = len(boom)
stack = []

def top(n):
    return stack[len(stack)-n:]

for i in range(len(word)):
    stack.append(word[i])

    if (len(stack) < lengthBoom): continue

    temp = ''.join(top(lengthBoom))

    if temp == boom:
        for _ in range(lengthBoom):
            stack.pop()

    # print(stack)
if (''.join(stack) == ''): print("FRULA")
else: print(''.join(stack))

#mirkovC4nizCC44
#C4