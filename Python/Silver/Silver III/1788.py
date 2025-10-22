n = int(input())

nabs = abs(n)

a, b = 0, 1
for i in range(2, nabs + 1):
    a, b = b, a + b
    # print(a, b)

fibpos = b

if (n == 0): 
    print(0)
    print(0)
elif (n > 0): 
    print(1)
    print(fibpos % 1000000000)
else: 
    print(pow(-1, nabs+1))
    print(fibpos % 1000000000)