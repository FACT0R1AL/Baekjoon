word = input()

n = int(input())
cnt = 0

for i in range(n):
    string = input()
    length = len(string)
    
    if word in string: cnt += 1
    else:
        for j in range(1, len(word)):
            temp = word[:j]
            temp2 = word[j:]
            
            if temp == string[length-j:length]:
                if temp2 == string[:len(word)-j]: cnt += 1

print(cnt)