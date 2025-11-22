n, quest = map(int, input().split())

arr = []
question = []

dictNum = {}
dictName = {}

for i in range(n):
    arr.append(input())

for i in range(quest):
    question.append(input())

for i in range(n):
    dictNum[i+1] = arr[i]
    dictName[arr[i]] = i+1

for q in question:
    if (q.isdigit()):
        print(dictNum[int(q)])
    else:
        print(dictName[q])
