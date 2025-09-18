n = int(input())
arr = list(str(n))
isSeven = 0

for i in range(len(arr)):
    if (arr[i] == '7'): 
        isSeven = 1
        break

if (isSeven == 0 and n%7 != 0): print(0)
elif (isSeven == 0 and n%7 == 0): print(1)
elif (isSeven == 1 and n%7 != 0): print(2)
elif (isSeven == 1 and n%7 == 0): print(3)