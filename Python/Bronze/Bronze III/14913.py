a, b, k = map(int, input().split())

find = a
cnt = 1
flag = False

while True:
    if (find == k):
        flag = True
        print(cnt)
        break

    find += b
    cnt += 1

    if (cnt >= 10000):
        break
    
if (flag == False):
    print("X")