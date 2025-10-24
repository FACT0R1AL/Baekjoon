length = int(input())

arr = list(input().split())
count = 0

existed = []

for a in arr:
    cheese = ''.join(a[-6:])

    if (cheese == "Cheese" and a not in existed): 
        count += 1
        existed.append(a)

if (count >= 4): print('yummy')
else: print('sad')