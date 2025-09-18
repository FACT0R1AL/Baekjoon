string = []
word = 'FBI'
count = 0

for i in range(5):
    string.append(input())

for i in range(5):
    flag = 0
    idx = 0
    length = len(string[i])

    for j in range(length):
        if (string[i][j] == word[idx]):
            idx += 1
        else: idx = 0

        if (idx == 3):
            flag = 1
            count += 1
            break

    if (flag): print(i+1, end=' ')

if (count == 0): print("HE GOT AWAY!")