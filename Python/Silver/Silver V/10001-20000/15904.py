short = 'UCPC'
arr = []
idx = 0

string = input()
length = len(string)

for i in range(length):
    if string[i] == short[idx]:
        arr.append(short[idx])
        idx += 1
    
    if idx == 4: break

if arr == ['U','C','P','C']: print("I love UCPC")
else: print("I hate UCPC")