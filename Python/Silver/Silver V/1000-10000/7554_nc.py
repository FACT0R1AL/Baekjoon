T = int(input())
answers = []

for t in range(1, T+1):
    length, *arr = map(int, input().split())

    count = 0

    for i in range(length):
        for j in range(i, length):
            if (arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                count += 1
    
    answers.append(count)

for t in range(1, T+1):
    print(f"Scenario #{t}:")
    print(answers[t-1])
    print()