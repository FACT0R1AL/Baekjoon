import sys

def roundAc(f):
    if (f%1 >= 0.5): return f//1+1
    else: return f//1
    
n = int(sys.stdin.readline().rstrip())
arr = []
delCount = int(roundAc(n*0.15))

for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()

for i in range(delCount):
    arr[i] = 0
    arr[n-i-1] = 0

if (n == 0): print(0)
else: print(int(roundAc(sum(arr)/(n-2*delCount))))