n = int(input())
binary = input()
k = int(input())

flag = True

if (k == 0 or binary == '0'): print("YES")

else:
    if ('1' in binary[-k:]): print("NO")
    else: print("YES")