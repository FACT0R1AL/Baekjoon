alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = int(input())

for _ in range(n):
    string = input()
    print(f"String #{_+1}")
    for i in range(len(string)):
        if (ord(string[i])-ord('A')+1 == 26): print("A", end='')
        else: print(alphabet[ord(string[i])-ord('A')+1], end = '')
    print('\n')