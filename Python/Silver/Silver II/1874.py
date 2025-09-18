from collections import deque

n = int(input())
arr = [int(input()) for _ in range(n)]

idx = 1
q = deque()
out = []
next = 0
flag = 0

for i in range(n):
    next = arr[i]

    if (len(q) > 0 and q[-1] == next):
        q.pop()
        out.append('-')
        
    else:
        while idx <= next:
            # print(f"{next} : {q}")
            q.append(idx)
            out.append('+')
            idx += 1
        
        if q[-1] != next: 
            flag=1
            break

        q.pop()
        out.append('-')
        # print(f"{next} : pop!!  {q}")     

if (flag): print("NO")
else:
    for o in out:
        print(o)