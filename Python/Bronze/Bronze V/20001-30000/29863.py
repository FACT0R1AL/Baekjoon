sleep = int(input())
wake = int(input())
cnt = 0

while (sleep <= 23 and sleep >= 20):
    cnt += 1
    sleep += 1
    
if (sleep != 24): print(wake-sleep)
else: print(wake+cnt)