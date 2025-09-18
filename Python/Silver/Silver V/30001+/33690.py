import math

n = int(input())
flag = 0
cnt = 0
arr = [0]

for m in range(1, 11):
    for i in range(1, 10):
        arr.append(int(str(i) * m))
        if (arr[-1] > n): 
            print(len(arr)-1)
            flag = 1
            break

    if (flag): break

# for i in range(n, -1, -1):
#     n = str(i)
#     n10 = str(math.floor(i/10))
    
#     length10 = len(n10)
#     length = len(n)



#     if (i < 10): 
#         print(f"{i} : possible")
#         cnt += 1

#     else:
#         flag = 1
#         for j in range(length):
#             if (n[j] != n[length - j - 1]): 
#                 flag = 0
#                 break
        
#         flag10 = 1
#         for j in range(length10):
#             if (n10[j] != n10[length10 - j - 1]):
#                 flag10 = 0
#                 break

#         if (flag and flag10):
#             print(f"{i} : possible")
#             cnt += 1
# print(cnt)