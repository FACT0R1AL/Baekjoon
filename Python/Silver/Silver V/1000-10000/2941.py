arr = [['c','='], ['c','-'], ['d','-'], ['l','j'], ['n','j'], ['s','='], ['z','=']]

string = input()
length = len(string)
i = 0

count = 0
string = list(string)

while (i < length):
    flag = 0
    stri2 = string[i:i+2]
    stri3 = string[i:i+3]

    if ['d','z','='] == stri3:
        i += 3
    else:     
        for j in range(len(arr)):
            if arr[j] == stri2:
                flag = 1
                break

        if (flag): i += 2
        else: i += 1

    count += 1

print(count)