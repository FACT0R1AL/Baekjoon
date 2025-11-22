n, k = map(int, input().split())

n -= 1
arr = [0 for _ in range(n)]

delcnt = 0
P = 2

while (1):
    for i in range(P-2, n, P):
        if (i < n and arr[i] != -1): 
            arr[i] = -1
            delcnt += 1

        if (delcnt == k):
            print(i+2)
            break


    if (delcnt == k):
        break

    for i in range(P-1, n):
        if (arr[i] == 0): 
            P = i+2
            break