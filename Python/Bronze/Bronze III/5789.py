T = int(input())

for _ in range(T):
    string = input()
    length = len(string)

    if (string[int(length/2)-1] == string[int(length/2)]): print('Do-it')
    else: print('Do-it-Not')