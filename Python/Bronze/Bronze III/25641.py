length = int(input())
string = input()

for i in range(length):
    S = string[i:].count('s')
    T = string[i:].count('t')

    if (S == T):
        print(string[i:])
        break