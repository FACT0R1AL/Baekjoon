t = int(input())

for i in range(t):
    string = list(input().split())

    for j in range(len(string)):
        for k in range(len(string[j])):
            print(string[j][len(string[j]) - k - 1], end='')

        print(' ', end='')